Add-Type -AssemblyName System.Drawing
$path = "D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage\UI_LimitLottery.png"
$bmp = New-Object System.Drawing.Bitmap($path)
$w = $bmp.Width
$h = $bmp.Height
$sum = 0
$cnt = 0
for ($y = 0; $y -lt $h; $y += 10) {
    for ($x = 0; $x -lt $w; $x += 10) {
        $c = $bmp.GetPixel($x, $y)
        $sum = $sum + ($c.R + $c.G + $c.B) / 3
        $cnt = $cnt + 1
    }
}
$avg = $sum / $cnt
Write-Host "Size: $w x $h"
Write-Host "Avg brightness: $avg"
$bmp.Dispose()