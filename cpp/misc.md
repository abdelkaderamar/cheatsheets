# using Howard Hinnant's library(https://howardhinnant.github.io/date/date.html)

std::chrono::system_clock::time_point tp = 
std::cout << date::format("%m/%d/%Y %I:%M:%S %p\n", tp);

