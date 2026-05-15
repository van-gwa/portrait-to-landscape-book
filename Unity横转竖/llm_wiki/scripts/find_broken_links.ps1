param([string]$VaultRoot = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki")
$linkPattern = '\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
$brokenLinks = @()
$mdFiles = Get-ChildItem -Path $VaultRoot -Filter "*.md" -Recurse -File
$linkRegex = [regex]::new($linkPattern)
foreach ($file in $mdFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $relPath = $file.FullName.Substring($VaultRoot.Length + 1)
    $matches = $linkRegex.Matches($content)
    foreach ($match in $matches) {
        $target = $match.Groups[1].Value.Trim()
        if ($target -match '^(http|https|mailto):' -or $target.StartsWith('#')) { continue }
        $sourceDir = Split-Path -Parent $file.FullName
        $targetClean = $target.Split('/') -join '\'
        $targetFile = Join-Path -Path $sourceDir -ChildPath $targetClean
        $found = $false
        foreach ($ext in '', '.md') {
            if (Test-Path "$targetFile$ext") { $found = $true; break }
        }
        if (-not $found) {
            $lineNum = ($content.Substring(0, $match.Index).Split("`n").Count)
            $brokenLinks += [PSCustomObject]@{
                SourceFile = $relPath
                LineNumber = $lineNum
                BrokenLink = $target
            }
        }
    }
}
if ($brokenLinks.Count -eq 0) {
    Write-Output "OK: No broken links found"
} else {
    Write-Output "ERROR: Found $($brokenLinks.Count) broken link(s):"
    foreach ($bl in $brokenLinks) {
        Write-Output "  [$($bl.SourceFile):$($bl.LineNumber)] -> '$($bl.BrokenLink)'"
    }
}
if ($brokenLinks.Count -gt 0) { exit 1 } else { exit 0 }