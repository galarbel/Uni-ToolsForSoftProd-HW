sig State {
	succ: some State
 }

sig  StateMachine {
	initalState: one State,
	reachable: set State
}{
	reachable = initalState.*succ
}

fact hasUnreachable {
	some s: State | s not in StateMachine.reachable
}


pred example {}

run example for exactly 1 StateMachine, 4 State
