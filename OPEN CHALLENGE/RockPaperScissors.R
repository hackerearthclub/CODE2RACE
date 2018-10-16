totalScore <- 0

choices <- c('Rock', 'Paper', 'Scissors')

scoreMatrix <- matrix(c(0,-1,1,1,0,-1,-1,1,0), 3, 3, byrow = TRUE)

scoreHands <- function(hand1, hand2) {
    # 1 wins, 0 ties, -1 looses (first hand relative to second)
    return(scoreMatrix[match(hand1, choices), match(hand2, choices)])
}

getPlayerHand <- function() {

    choice <- NA

    while(!choice %in% choices) {
        cat("Please choose one of: ", paste(choices, collapse = ", "))
        cat("\nYour choice: ")
        choice <- readLines("stdin",1)
    }

    return(choice);
}

updateScore <- function(score, totalScore) {
    return(totalScore + score)
}

aftermath <- function(score, totalScore) {
    cat(c("Sorry, you were bested...","It's a tie!","You won this hand!")[score+2])
    cat("\nYou have ", totalScore, " points more than your opponent.\n\n")
}

getQuit <- function() {
    cat("Do you want to play again?\n")
    string <- readLines("stdin", 1)
    cat("\n")
    return(string %in% c("no","No","NO","n","N","quit","Quit","QUIT","q","Q"))
}

gameover <- FALSE;

while(!gameover) {

    playerHand <- getPlayerHand()
    computerHand <- sample(choices, 1)
    cat(paste("Computer chose:", computerHand, "\n"))
    score <- scoreHands(playerHand, computerHand)
    totalScore <- updateScore(score, totalScore)
    aftermath(score, totalScore)
    gameover <- getQuit()
}

cat("Thanks for playing!\n")
