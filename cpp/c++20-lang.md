main_title: C++20 Language New Features Cheatsheet
lang: cpp

#-------------------------------------------------------------------------------
title: Designated initializers
struct book_config_t {
  double total_amount;
  double order_amount;
}
book_config_t config {
 .total_amount = total_amount,
 .order_amount = order_amount
}
#-------------------------------------------------------------------------------
title: Template in lambda
auto add = [&]<typename T>(T sum,
                           const book_row_t& row)
{ return sum + (_last_share_price*row.qty); };
#-------------------------------------------------------------------------------
title: using enum
enum class frequency_type {
  NONE,
  DAILY,
  WEEKLY,
  MONTHLY
};
switch (frequency) {
  using enum frequency_type;
  {
    case NONE: break;
    case DAILY: break;
    case WEEKLY: break;
    case MONTHLY: break;
  }
}
#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
title: 

#-------------------------------------------------------------------------------
