#Term Frequency (TF)
tf <- function(row){
  return(row/sum(row))
}

#Inverse Document Frequency (IDF)
idf <- function(col){
  return(log10(length(col)/length(which(col>0))))
}


#Term Frequency - Inverse Document Frequency (TF-IDF)
tfidf <- function(token.matrix){
  
  tf <- t(apply(token.matrix, 1, tf))
  idf <- apply(token.matrix, 2, idf)
  
  return(tf*idf)
  
}

#Testing the Function
library(tm)
text <- c("a dog and a cat", "The dog is barking", "The cat is on the wall")

#Creating a Corpus
corp <- Corpus(VectorSource(text))

#Finding the tokens
doc.tokens <- as.matrix(DocumentTermMatrix(corp))

#Calling the tfidf function the matrix
tfidf(doc.tokens)
