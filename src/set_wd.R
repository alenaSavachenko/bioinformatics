
library(rbbt)

bookdown::render_book()


library('RPostgreSQL')
library("remotes")
library("RPostgres")

con <- dbConnect(RPostgres::Postgres(),
                 dbname = "workflowsdb",
                 host="localhost",
                 port="5432",
                 user="postgres",
                 password="admin")





# Install the required package
install.packages("readr")
# Load the installed Package
library(readr)
library(tidyverse)


mart_export<-read_tsv("data/les2/mart_export.txt") %>%   janitor::clean_names()

head(mart_export)


mutation_data <-  read_tsv("data/les2/BKM120_Mutation_Data.tsv")   %>%  janitor::clean_names()

head(mutation_data)



dbWriteTable(con, "mart_export",mart_export)

dbWriteTable(con, "mutation_data", mutation_data)

dbListTables(con)


data <-  read_tsv("output/mutation_data_mart_export_202411132102.txt")

head(data)

nrow(data)

nrow(mutation_data)


library(fs)

fs::dir_tree(here::here())


fs::dir_tree("C:/Users/Mijn-PC/Documents/r/Daur2")


#git clone https://github.com/alenagrrr3/projecticum.git

fs::dir_tree("C:/Users/Mijn-PC/Documents/r/projecticum")





