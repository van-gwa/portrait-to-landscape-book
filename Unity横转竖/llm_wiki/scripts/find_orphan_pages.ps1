param([string]$VaultRoot = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki")
$linkPattern = '\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
$mdFiles = Get-ChildItem -Path $VaultRoot -Filter "*.md" -Recurse -File
$linkRegex = [regex]::new($linkPattern)
$linkedPages = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
foreach ($file in $mdFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $matches = $linkRegex.Matches($content)
    foreach ($match in $matches) {
        $target = $match.Groups[1].Value.Trim()
        if ($target -match '^(http|https|mailto):' -or $target.StartsWith('#')) { continue }
        $pageName = ($target.Split('/'))[-1]
        [void]$linkedPages.Add($pageName)
    }
}
$orphanPages = @()
foreach ($file in $mdFiles) {
    $fileName = Split-Path -Leaf $file.FullName
    if ($fileName -eq "README.md") { continue }
    $pageNameNoExt = $fileName -replace '\.md$', ''
    if (-not $linkedPages.Contains($pageNameNoExt)) {
        $relPath = $file.FullName.Substring($VaultRoot.Length + 1)
        $orphanPages += $relPath
    }
}
if ($orphanPages.Count -eq 0) {
    Write-Output "OK: No orphan pages found"
} else {
    Write-Output "WARN: $($orphanPages.Count) orphan page(s):"
    foreach ($p in $orphanPages) { Write-Output "  - $p" }
}
if ($orphanPages.Count -gt 0) { exit 1 } else { exit 0 }