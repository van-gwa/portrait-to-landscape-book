Add-Type -AssemblyName System.Drawing
$imgPath = "D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage\UI_LimitLottery.png"
$exists = Test-Path $imgPath
Write-Host "Path exists: $exists"
if ($exists) {
    $bmp = New-Object System.Drawing.Bitmap($imgPath)
    $w = $bmp.Width
    $h = $bmp.Height
    Write-Host "Size: $w x $h"
    $bmp.Dispose()
}