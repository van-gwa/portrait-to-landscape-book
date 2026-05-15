$ErrorActionPreference = 'SilentlyContinue'
$dir = 'D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types'
Get-ChildItem $dir -Name | ForEach-Object {
    $f = $_
    $path = $dir + '\' + $f
    $content = Get-Content $path -Raw
    if ($content -match 'LimitLottery') {
        Write-Host $f
    }
}