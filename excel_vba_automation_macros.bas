Attribute VB_Name = "B2BAutomationMacros"
' ==========================================================================
' Excel VBA Automation Suite Pro - 1-Click Consolidation & Lead Cleaning
' Author: Tung Nguyen (@tungnguyen84)
' Custom Excel VBA & Dashboards: https://www.fiverr.com/s/bd4m6V0
' ==========================================================================

Public Sub CleanAndDeduplicateLeads()
    Dim ws As Worksheet
    Dim lastRow As Long, i As Long
    Application.ScreenUpdating = False
    Set ws = ActiveSheet
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    If lastRow > 1 Then
        For i = 2 To lastRow
            ws.Cells(i, 3).Value = LCase(Trim(ws.Cells(i, 3).Value))
        Next i
        ws.Range("A1:K" & lastRow).RemoveDuplicates Columns:=Array(2), Header:=xlYes
    End If
    ws.Columns.AutoFit
    Application.ScreenUpdating = True
    MsgBox "Cleaned and deduplicated B2B leads successfully!", vbInformation
End Sub

Public Sub ConsolidateAllSheetsToMaster()
    Dim ws As Worksheet, masterWs As Worksheet
    Dim lastRow As Long, lastCol As Long, destRow As Long
    Application.ScreenUpdating = False
    On Error Resume Next
    Set masterWs = ThisWorkbook.Worksheets("Master_Consolidated")
    If masterWs Is Nothing Then
        Set masterWs = ThisWorkbook.Worksheets.Add(Before:=ThisWorkbook.Worksheets(1))
        masterWs.Name = "Master_Consolidated"
    Else
        masterWs.Cells.Clear
    End If
    On Error GoTo 0
    destRow = 1
    For Each ws In ThisWorkbook.Worksheets
        If ws.Name <> masterWs.Name And ws.UsedRange.Rows.Count > 1 Then
            lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
            lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
            If destRow = 1 Then
                ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol)).Copy masterWs.Cells(1, 1)
                destRow = lastRow + 1
            Else
                ws.Range(ws.Cells(2, 1), ws.Cells(lastRow, lastCol)).Copy masterWs.Cells(destRow, 1)
                destRow = destRow + (lastRow - 1)
            End If
        End If
    Next ws
    masterWs.Columns.AutoFit
    Application.ScreenUpdating = True
    MsgBox "Consolidated all sheets into Master_Consolidated (" & (destRow - 1) & " rows)!", vbInformation
End Sub
