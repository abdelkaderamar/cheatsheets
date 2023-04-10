main_title: CSS selector cheatsheets
lang: css
#-------------------------------------------------------------------------------
title: Get element with a class
element.class
Example: div.product to get all divs of class product
#-------------------------------------------------------------------------------
title: Get the text of an element 
element::text
Example: div::text
#-------------------------------------------------------------------------------
title: Get the text of an element with a class 
element.class::text
Example: div.product-subtitle::text
#-------------------------------------------------------------------------------
title: Get the elements depending on the parent
element>element
Example: div>img select img elements where the parent is a div
#-------------------------------------------------------------------------------
title: Get the attribute depending on the parent class
element.class>element::attr(attr_name)
Example: div.thumbnail>img::attr(data-src) select data-src attribute of img 
elements where the parent is a div with the class thumbnail
#-------------------------------------------------------------------------------
