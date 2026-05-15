Add-Type -AssemblyName System.Drawing

# Get the file listing
$folder = "D:\CursorProject\Dadian - 副本\Arts\Doc\UIImage"
$allFiles = Get-ChildItem -Path $folder -Filter "UI_LimitLottery.png" -ErrorAction SilentlyContinue
Write-Host "Files found: $($allFiles.Count)"

if ($allFiles.Count -gt 0) {
    $fullPath = $allFiles[0].FullName
    Write-Host "FullPath: $fullPath"

    $bmp = New-Object System.Drawing.Bitmap($fullPath)
    $w = $bmp.Width
    $h = $bmp.Height
    Write-Host "Size: $w x $h"

    $step = 20
    $cells = @{}
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
    $topActive = 0; $midActive = 0; $bottomActive = 0
    $leftActive = 0; $rightActive = 0
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
            if ($c -lt ($colCount / 2)) { $leftActive += $cnt } else { $rightActive += $cnt }
        }
    }

    Write-Host "Non-black cells: $activeCells / $totalCells"
    Write-Host "Top/Mid/Bottom: $topActive / $midActive / $bottomActive"
    Write-Host "Left/Right: $leftActive / $rightActive"

    $rowCounts = @{}
    for ($r = 0; $r -lt $rowCount; $r++) {
        $cnt = 0
        for ($c = 0; $c -lt $colCount; $c++) {
            if ($cells.containsKey("$r-$c")) { $cnt++ }
        }
        if ($cnt -gt 0) { $rowCounts[$r] = $cnt }
    }

    $colCounts = @{}
    for ($c = 0; $c -lt $colCount; $c++) {
        $cnt = 0
        for ($r = 0; $r -lt $rowCount; $r++) {
            if ($cells.containsKey("$r-$c")) { $cnt++ }
        }
        if ($cnt -gt 0) { $colCounts[$c] = $cnt }
    }

    $maxRowCells = if ($rowCounts.Values.Count -gt 0) { ($rowCounts.Values | Measure-Object -Maximum).Maximum } else { 0 }
    $maxColCells = if ($colCounts.Values.Count -gt 0) { ($colCounts.Values | Measure-Object -Maximum).Maximum } else { 0 }
    Write-Host "MaxRowCells: $maxRowCells, MaxColCells: $maxColCells"

    $bmp.Dispose()
} else {
    Write-Host "UI_LimitLottery.png not found in folder"
}