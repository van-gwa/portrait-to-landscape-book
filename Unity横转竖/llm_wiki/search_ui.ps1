$results = Select-String -Path 'D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types\*.md' -Pattern 'UI_LimitLottery'
foreach ($r in $results) {
    Write-Host "File: $($r.Filename)"
    Write-Host "Line $($r.LineNumber): $($r.Line)"
    Write-Host "---"
}