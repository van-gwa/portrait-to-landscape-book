param(
    [string]$VaultRoot = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki",
    [string]$OutputFile = ""
)
$wikiRoot = $VaultRoot
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$dateStr = Get-Date -Format "yyyy-MM-dd"
if ($OutputFile -eq "") {
    $OutputFile = Join-Path $wikiRoot "qa\lint_reports\lint_report_$dateStr.md"
}
$outDir = Split-Path -Parent $OutputFile
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}
$sb = [System.Text.StringBuilder]::new()
$null = $sb.AppendLine("# Wiki Health Report")
$null = $sb.AppendLine("")
$null = $sb.AppendLine("**Generated**: $timestamp")
$null = $sb.AppendLine("**Wiki root**: $wikiRoot")
$null = $sb.AppendLine("")
$mdFiles = Get-ChildItem -Path $wikiRoot -Filter "*.md" -Recurse -File
$totalFiles = $mdFiles.Count
$null = $sb.AppendLine("## Overview")
$null = $sb.AppendLine("")
$null = $sb.AppendLine("| Metric | Value |")
$null = $sb.AppendLine("|--------|-------|")
$null = $sb.AppendLine("| Total pages | $totalFiles |")
$null = $sb.AppendLine("")
$linkPattern = '\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
$linkRegex = [regex]::new($linkPattern)
$brokenLinks = @()
foreach ($file in $mdFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
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
            $brokenLinks += [PSCustomObject]@{Source = (Split-Path -Leaf $file.FullName); Link = $target}
        }
    }
}
$null = $sb.AppendLine("## Broken Links")
$null = $sb.AppendLine("")
if ($brokenLinks.Count -eq 0) {
    $null = $sb.AppendLine("OK: No broken links found ($totalFiles pages checked)")
} else {
    $null = $sb.AppendLine("WARN: $($brokenLinks.Count) broken link(s) found:")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("| Source | Broken Link |")
    $null = $sb.AppendLine("|--------|-------------|")
    foreach ($bl in $brokenLinks) {
        $null = $sb.AppendLine("| $($bl.Source) | ``[[$($bl.Link)]]`` |")
    }
}
$null = $sb.AppendLine("")
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
        $orphanPages += $fileName
    }
}
$null = $sb.AppendLine("## Orphan Pages (no inbound links)")
$null = $sb.AppendLine("")
if ($orphanPages.Count -eq 0) {
    $null = $sb.AppendLine("OK: All pages have inbound links")
} else {
    $null = $sb.AppendLine("WARN: $($orphanPages.Count) orphan page(s):")
    $null = $sb.AppendLine("")
    foreach ($op in $orphanPages) {
        $null = $sb.AppendLine("- $op")
    }
}
$null = $sb.AppendLine("")
$fmPattern = '^---\r?\n([\s\S]*?)\r?\n---'
$fmRegex = [regex]::new($fmPattern)
$missingFM = @()
$noType = @()
foreach ($file in $mdFiles) {
    $fileName = Split-Path -Leaf $file.FullName
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $fmMatch = $fmRegex.Match($content)
    if (-not $fmMatch.Success) {
        $missingFM += $fileName
        continue
    }
    if ($fmMatch.Groups[1].Value -notmatch 'type:') {
        $noType += $fileName
    }
}
$null = $sb.AppendLine("## Frontmatter Check")
$null = $sb.AppendLine("")
$null = $sb.AppendLine("| Issue | Count |")
$null = $sb.AppendLine("|-------|-------|")
$null = $sb.AppendLine("| Missing frontmatter entirely | $($missingFM.Count) |")
$null = $sb.AppendLine("| Missing type field | $($noType.Count) |")
$null = $sb.AppendLine("")
if ($missingFM.Count -gt 0) {
    $null = $sb.AppendLine("**Pages missing frontmatter:**")
    foreach ($p in $missingFM) { $null = $sb.AppendLine("- $p") }
    $null = $sb.AppendLine("")
}
if ($noType.Count -gt 0) {
    $null = $sb.AppendLine("**Pages missing type field:**")
    foreach ($p in $noType) { $null = $sb.AppendLine("- $p") }
    $null = $sb.AppendLine("")
}
$score = 100
if ($brokenLinks.Count -gt 0) { $score -= [Math]::Min(30, $brokenLinks.Count * 2) }
if ($orphanPages.Count -gt 0) { $score -= [Math]::Min(20, $orphanPages.Count) }
if ($missingFM.Count -gt 0) { $score -= [Math]::Min(25, $missingFM.Count) }
if ($noType.Count -gt 0) { $score -= [Math]::Min(25, $noType.Count) }
$score = [Math]::Max(0, $score)
$null = $sb.AppendLine("## Health Score")
$null = $sb.AppendLine("")
$null = $sb.AppendLine("**Score: $score / 100**")
$null = $sb.AppendLine("")
if ($score -ge 90) {
    $null = $sb.AppendLine("Green - Wiki health is good")
} elseif ($score -ge 70) {
    $null = $sb.AppendLine("Yellow - Minor issues to fix")
} elseif ($score -ge 50) {
    $null = $sb.AppendLine("Orange - Needs attention")
} else {
    $null = $sb.AppendLine("Red - Needs urgent attention")
}
$null = $sb.AppendLine("")
$null = $sb.AppendLine("---")
$null = $sb.AppendLine("*Generated by lint_report.ps1*")
$sb.ToString() | Out-File -FilePath $OutputFile -Encoding UTF8
Write-Output "Report: $OutputFile"
Write-Output "Score: $score/100 | Broken:$($brokenLinks.Count) | Orphans:$($orphanPages.Count) | NoFM:$($missingFM.Count) | NoType:$($noType.Count)"