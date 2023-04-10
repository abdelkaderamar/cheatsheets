main_title: Latex Cheatsheet
lang: latex

#------------------------------------------------------------------------------
#- section: Text Properties
#------------------------------------------------------------------------------
title: Fonts
\textrm{Roman}
\textsf{Sans serif}
\texttt{Typewriter}
\textmd{Medium series}
\textbf{Bold series}
\textup{Upright shape}
\textit{Italic shape}
\textsl{Slanted shape}
\textsc{Small Caps shape}
\emph{Emphasized}
\textnormal{Document font}
\underline{Underline}
#------------------------------------------------------------------------------
title: Size
\tiny \scriptsize \footnotesize \small \normalsize
\large \Large \LARGE \huge \Huge
#------------------------------------------------------------------------------
#- section: Multiple Columns
#------------------------------------------------------------------------------
title: Multiple columns
\usepackage{multicol}
% column separation set to 1cm
\setlength{\columnsep}{1cm}
% insert a blue vertical rulers (add color package)
\setlength{\columnseprule}{1pt}
\def\columnseprulecolor{\color{blue}}
% use multicols* for unbalanced columns
\begin{multicols}{3}
["Header text", which is inserted in between square
brackets. This is optional and will be displayed on
top of the multicolumn text.]
% insert a column breakpoint
\columnbreak
\end{multicols}
#------------------------------------------------------------------------------
#- section: Tabular
#------------------------------------------------------------------------------
title: Multiple line in some cells: p-type column
\begin{tabular}{l|p{15mm}}
\hline
foo & bar \newline rlz \\
\hline
\end{tabular}
#------------------------------------------------------------------------------
title: Multiple line in some cells: tabular within tabular
\begin{tabular}{cccc}
One & Two & Three & Four \\
Een & Twee & Drie & Vier \\
One & Two &
\begin{tabular}{@{}c@{}}
Three \\ Drie\end{tabular}
& Four
\end{tabular}
#------------------------------------------------------------------------------
title: Multiple line in some cells: \shortstack
\begin{tabular}{ccc}
one & two & three \\
one & two & \shortstack{aa \\ bb}\\
\end{tabular}
#------------------------------------------------------------------------------
title:

#------------------------------------------------------------------------------
title:

#------------------------------------------------------------------------------
title:

#------------------------------------------------------------------------------
