Add-Type -AssemblyName System.Drawing
$path = "D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage\UI_LimitLottery.png"
if (Test-Path $path) {
    $bmp = New-Object System.Drawing.Bitmap($path)
    $w = $bmp.Width
    $h = $bmp.Height
    $topBright = 0
    $midBright = 0
    $bottomBright = 0
    $leftBright = 0
    $rightBright = 0
    for ($y = 0; $y -lt $h; $y += 5) {
        for ($x = 0; $x -lt $w; $x += 5) {
            $c = $bmp.GetPixel($x, $y)
            $bright = ($c.R + $c.G + $c.B) / 3
            if ($bright -gt 30) {
                if ($y -lt ($h * 0.33)) { $topBright = $topBright + 1 }
                elseif ($y -lt ($h * 0.66)) { $midBright = $midBright + 1 }
                else { $bottomBright = $bottomBright + 1 }
                if ($x -lt ($w * 0.5)) { $leftBright = $leftBright + 1 }
                else { $rightBright = $rightBright + 1 }
            }
        }
    }
    Write-Host "Size: $w x $h"
    Write-Host "Top: $topBright, Mid: $midBright, Bottom: $bottomBright"
    Write-Host "Left: $leftBright, Right: $rightBright"
    $bmp.Dispose()
} else {
    Write-Host "NOT FOUND"
}