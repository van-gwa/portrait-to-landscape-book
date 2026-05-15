$files = @(
    "UI_AcitveAd.png",
    "UI_ActApexPvp.png",
    "UI_ActArena.png",
    "UI_Bag.png",
    "UI_BattlePassRewardOverview.png",
    "UI_Beauty.png",
    "UI_LimitActivity.png",
    "UI_LimitLottery.png",
    "UI_PirateEvent.png",
    "UI_SnowWheel.png",
    "UI_AssistantPanel.png"
)
$idx = Get-Random -Minimum 0 -Maximum $files.Count
$selected = $files[$idx]
Write-Host "Selected: $selected"