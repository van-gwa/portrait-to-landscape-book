$folder = 'D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types'
$files = Get-ChildItem -Path $folder -Filter '*.md'
$counter = 0
$total = $files.Count
foreach ($f in $files) {
    $counter++
    $content = Get-Content $f.FullName -Raw -Encoding utf8
    if ($content -match 'UI_LimitLottery') {
        Write-Host "Found in: $($f.Name)"
        Write-Host "Match count: $(($content | Select-String -Pattern 'UI_LimitLottery' -AllMatches).Matches.Count)"
    }
    if ($counter % 20 -eq 0) { Write-Host "Processed $counter / $total" }
}
Write-Host "Done. Total files: $total"