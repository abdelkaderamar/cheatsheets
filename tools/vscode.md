main_title: VSCode Cheatsheet
lang: text

#------------------------------------------------------------------------------
title: Switch between source/header file
Alt - O
#------------------------------------------------------------------------------
title: Fold the level [n] (0 to fold all)
   Ctrl - k / Ctrl [n]
Unfold all
   Ctrl - k / Ctrl j
#------------------------------------------------------------------------------
title: Shortcut to switch between editor/terminal
Open keybindings.json (using Ctrl+Shift+P then
Open Keyboard Shortcuts File) and add the following
{
  "key": "shift+alt+t",
  "command": "workbench.action.terminal.focus"
},
{
  "key": "shift+alt+t",
  "command":
    "workbench.action.focusActiveEditorGroup",
  "when": "terminalFocus"
}
#------------------------------------------------------------------------------


