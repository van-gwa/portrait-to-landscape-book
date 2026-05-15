Add-Type -AssemblyName System.Drawing

$path = 'D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage\UI_LimitLottery.png'
$fullPath = (Get-ChildItem $path).FullName

$bmp = New-Object System.Drawing.Bitmap($fullPath)
$w = $bmp.Width
$h = $bmp.Height

Write-Host "Image: UI_LimitLottery.png"
Write-Host "Size: $w x $h"

# Analyze distribution: top/middle/bottom thirds, left/right halves
$step = 20
$cells = @{}  # key = "r-c", value = count of non-black pixels

for ($y = 0; $y -lt $h; $y += $step) {
    $row = [Math]::Floor($y / $step)
    for ($x = 0; $x -lt $w; $x += $step) {
        $col = [Math]::Floor($x / $step)
        $c = $bmp.GetPixel($x, $y)
        if ($c.R -gt 20 -or $c.G -gt 20 -or $c.B -gt 20) {
            $key = "$row-$col"
            if (-not $cells.ContainsKey($key)) { $cells[$key] = 0 }
            $cells[$key]++
        }
    }
}

$totalCells = 0
$activeCells = 0
$topActive = 0
$midActive = 0
$bottomActive = 0
$leftActive = 0
$rightActive = 0

$rowCount = [Math]::Ceiling($h / $step)
$colCount = [Math]::Ceiling($w / $step)

for ($r = 0; $r -lt $rowCount; $r++) {
    for ($c = 0; $c -lt $colCount; $c++) {
        $key = "$r-$c"
        $cnt = if ($cells.ContainsKey($key)) { $cells[$key] } else { 0 }
        $totalCells++
        if ($cnt -gt 0) { $activeCells++ }
        if ($r -lt 3) { $topActive += $cnt }
        elseif ($r -lt 6) { $midActive += $cnt }
        else { $bottomActive += $cnt }
        if ($c -lt ($colCount / 2)) { $leftActive += $cnt }
        else { $rightActive += $cnt }
    }
}

Write-Host ""
Write-Host "Non-black pixel cells: $activeCells / $totalCells"
Write-Host "Top third: $topActive, Mid third: $midActive, Bottom third: $bottomActive"
Write-Host "Left half: $leftActive, Right half: $rightActive"
Write-Host "Left vs Right ratio: $([Math]::Round($leftActive * 100 / ($rightActive + 1)))%"

# Check for horizontal list pattern (many cells in same row)
$rowCounts = @{}
for ($r = 0; $r -lt $rowCount; $r++) {
    $cnt = 0
    for ($c = 0; $c -lt $colCount; $c++) {
        $key = "$r-$c"
        if ($cells.containsKey($key)) { $cnt++ }
    }
    if ($cnt -gt 0) { $rowCounts[$r] = $cnt }
}
$maxRowCells = ($rowCounts.Values | Measure-Object -Maximum).Maximum
Write-Host "Max active cells in a single row: $maxRowCells (suggests horizontal list if high)"

# Check vertical list pattern
$colCounts = @{}
for ($c = 0; $c -lt $colCount; $c++) {
    $cnt = 0
    for ($r = 0; $r -lt $rowCount; $r++) {
        $key = "$r-$c"
        if ($cells.containsKey($key)) { $cnt++ }
    }
    if ($cnt -gt 0) { $colCounts[$c] = $cnt }
}
$maxColCells = ($colCounts.Values | Measure-Object -Maximum).Maximum
Write-Host "Max active cells in a single col: $maxColCells (suggests vertical list if high)"

$bmp.Dispose()

Write-Host ""
Write-Host "=== Visual Analysis Summary ==="
if ($rightActive -gt ($leftActive * 1.5)) {
    Write-Host "Layout: Right-heavy (possible left image + right list)"
} elseif ($leftActive -gt ($rightActive * 1.5)) {
    Write-Host "Layout: Left-heavy (possible left list + right image)"
} else {
    Write-Host "Layout: Balanced or centered"
}
if ($topActive -gt ($bottomActive * 2)) {
    Write-Host "Content: Top-distributed"
} elseif ($bottomActive -gt ($topActive * 2)) {
    Write-Host "Content: Bottom-distributed"
} else {
    Write-Host "Content: Evenly distributed"
}
if ($maxColCells -gt 5) {
    Write-Host "Pattern: Vertical list detected"
} elseif ($maxRowCells -gt 5) {
    Write-Host "Pattern: Horizontal list detected"
} else {
    Write-Host "Pattern: Scattered/grid"
}