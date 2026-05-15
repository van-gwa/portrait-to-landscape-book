$files = Get-ChildItem 'D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types\' -Name
foreach ($f in $files) {
    $content = Get-Content "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types\$f" -Encoding UTF8 -Raw
    if ($content -match 'ActArena|arena') {
        Write-Output $f
    }
}
