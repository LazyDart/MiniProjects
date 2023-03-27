setwd("C:\\Users\\User\\Desktop\\Na State z R")

install.packages("dplyr")
install.packages("stringr")
install.packages("DT")
install.packages("ggplot2")
install.packages("EnvStats")


top_movies <- read.csv("movies.csv")




variable.names(top_movies)


??str_split()

testowy_cast <- str_split(top_movies$cast_name[1], ",", simplify = TRUE)


testowy_cast[1]


top_movies <- top_movies %>% 
  mutate(first_cast = str_split(cast_name, ",", simplify = TRUE)[, 1]) %>%
  mutate(second_cast = str_split(cast_name, ",", simplify = TRUE)[, 2]) %>% 
  mutate(third_cast = str_split(cast_name, ",", simplify = TRUE)[, 3]) %>% 
  mutate(fourth_cast = str_split(cast_name, ",", simplify = TRUE)[, 4]) %>% 
  mutate(fifth_cast = str_split(cast_name, ",", simplify = TRUE)[, 5]) 

top_movies <- datatable(top_movies)

top_movies.columns








