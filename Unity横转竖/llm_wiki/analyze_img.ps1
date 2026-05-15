Add-Type -AssemblyName System.Drawing
$imgPath = 'D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage\UI_LimitLottery.png'
if (Test-Path $imgPath) {
    $bmp = New-Object System.Drawing.Bitmap($imgPath)
    $w = $bmp.Width
    $h = $bmp.Height
    Write-Host "Image: UI_LimitLottery.png"
    Write-Host "Size: $w x $h"
    
    # Sample pixel distribution
    $stepX = [int]($w / 10)
    $stepY = [int]($h / 10)
    
    $topPixels = 0
    $midPixels = 0
    $bottomPixels = 0
    $leftPixels = 0
    $rightPixels = 0
    
    for ($y = 0; $y -lt $h; $y += $stepY) {
        for ($x = 0; $x -lt $w; $x += $stepX) {
            $c = $bmp.GetPixel($x, $y)
            $bright = ($c.R + $c.G + $c.B) / 3
            if ($bright -gt 30) {
                if ($y -lt ($h * 0.33)) { $topPixels++ }
                elseif ($y -lt ($h * 0.66)) { $midPixels++ }
                else { $bottomPixels++ }
                
                if ($x -lt ($w * 0.5)) { $leftPixels++ }
                else { $rightPixels++ }
            }
        }
    }
    Write-Host "Top: $topPixels, Mid: $midPixels, Bottom: $bottomPixels"
    Write-Host "Left: $leftPixels, Right: $rightPixels"
    
    # Check for horizontal vs vertical list
    $horizCount = 0
    $vertCount = 0
    $prevY = -1
    for ($y = 0; $y -lt $h; $y += 5) {
        $rowBright = 0
        for ($x = 0; $x -lt $w; $x += 5) {
            $c = $bmp.GetPixel($x, $y)
            $rowBright += ($c.R + $c.G + $c.B) / 3
        }
        $avg = $rowBright / ($w / 5)
        if ($avg -gt 30) {
            if ($prevY -ge 0 -and ($y - $prevY) -gt 30) { $vertCount++ }
            $prevY = $y
        }
    }
    Write-Host "Potential vertical item count: $vertCount"
    
    $bmp.Dispose()
} else {
    Write-Host "File not found"
}