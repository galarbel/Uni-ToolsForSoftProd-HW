sig State {
	succ: one State
 }

sig  StateMachine {
	initalState: one State
}

pred example {}

run example for exactly 1 StateMachine, 4 State
