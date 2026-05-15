Get-ChildItem 'D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types\' -File -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
    if ($content -match 'LimitLottery') {
        Write-Host $_.Name
    }
}