
/*
 =================================================================
 FILE...............: tennisSimulator.go
 DESCRIPTION........: Program to simulate a simple tennis 1v1 match in Go lang.
						Rules: 
							- The first player to made 4 points wins if the difference between
								the player's scores are equal or greater than 2.
 AUTHOR.............: Erick Silva (https://github.com/erickos)
 CREATED IN.........: 20/06/2018
 MODIFIED IN........: 24/06/2018
 =================================================================
*/

package main

import (
	"math/rand"
	"time"
	"fmt"
)

// Struct representing a Tennis Player
type Player struct {
	name string
	points int
}

/**
 *	Generates a random int number between the [min,max] interval
 */
func random(min, max int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(max - min) + min
}

/**
 * Prints the scoreboard of the match
 */
func printScoreboard( player1 *Player, player2 *Player ) {
	fmt.Printf( "\n>>>SCOREBOARD<<<\n(%s)  %d  x  %d  (%s)\n\n", player1.name, player1.points, player2.points, player2.name)
}

/**
 * Makes the round attack of the player. The 'player' add on channel a int representing the position of the
 *		ball in the tennis court.
 */
func attack( ch chan<-int, player *Player ) {
	fmt.Printf("%s is attacking now\n", player.name)
	areaBall := random( 1,3 ) // area where the ball will be attacked

	ch <- areaBall // send by channel.
}

/**
 * Defends the ball recently attacked and is on channel.
 *	First: generates a random position on the court to player defend;
 * 	Second: reads the position on channel, that is the position where the ball is;
 *	Third: If the (FIRST) is equal than the position readed in channel, then the pĺayer had sucess to defend, insucess in otherwise
 */
func def( ch chan int, player *Player, success *bool ) {
	fmt.Printf("%s is trying to defend the ball\n", player.name)
	areaPlayer := random( 1,3 ) // area where the player will defend
	areaBall := <- ch 	    // area where is the ball

	if areaPlayer == areaBall {
		fmt.Printf("%s has defended the ball\n", player.name)
		*success = true
	} else {
		fmt.Printf("%s missed the ball\n", player.name)
		*success = false
	}
}

/**
 * Realizes a move of the match, that is a attack by a attackPlayer and a defense by the defendPlayer
 */
func move( attackPlayer *Player, defendPlayer *Player, ch chan int ) bool {
	var successDef bool
	go attack( ch, attackPlayer )
	time.Sleep(1e9) // waits the attack
	go def( ch, defendPlayer, &successDef)
	time.Sleep(1e9) // waits a defense
	if !successDef { // if the the defense attempt has fail then increment the points of the attacker
		pontuate( attackPlayer )
	}
	time.Sleep(1e9)

	return successDef
}

/**
 * Increment the player pontuation on sucessfull attack
 */
func pontuate( attackingPlayer *Player ) {
	attackingPlayer.points++
}

/**
 * Verify if the between the players has a winner. That is a player must have 4 or more points and a difference of 2 or more points.
 */
func hasWinner( player1 *Player, player2 *Player ) bool {

	if player1.points >= 4 || player2.points > 4 {
		if (player1.points - player2.points) >= 2 || (player2.points - player1.points) >= 2 {
			return true
		}
	}

	return false
}

/**
 * Get the winner and loser players
 */
func getWinner( player1 *Player,  player2 *Player ) (Player, Player) {
	if player1.points >= player2.points { // Keeps the player with more points
		return *player1, *player2
	}

	return *player2, *player1
}


/**
 *  Execute the match between two players.
 */
func play( player1 *Player, player2 *Player, ch chan int ) (Player, Player) {

	for !hasWinner( player1, player2 ) { // while not have a winner
		sucessfullDefense := move( player1, player2, ch )
		if sucessfullDefense {  // if the ball has been defended, swap the players
			aux := player1 		// That is the players was on attack, now is defending
			player1 = player2	// 	And the defender, now is attacking
			player2 = aux
		}
		printScoreboard( player1, player2 ) // show the scoreboard every round
	}
	winner, loser := getWinner( player1, player2 ) // gets the winner and loser
	return winner, loser // return them
}


/**
 * Main function, effectively executes the program
 */
func main() {
	fmt.Println(">>> Starting the tennis match <<< ")

	players := []Player{ {"Guga", 0 }, { "Thomaz Bellucci", 0 } } // slice of players

	ch := make( chan int ) // makes the channel

	winner, loser := play( &players[0], &players[1], ch ) // init the match


	fmt.Printf("\t>>>FINAL SCOREBOARD<<<\n>(%s)<  %d  x  %d  (%s)\n\n", winner.name, winner.points, loser.points, loser.name)
	fmt.Printf( "\n>>>> The winner is %s <<<<\n", winner.name)
}
