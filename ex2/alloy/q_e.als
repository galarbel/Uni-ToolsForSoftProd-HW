sig State {
	succ: set State
}

sig  StateMachine {
	initalState: one State,
	machineReachable: set State
}{
	machineReachable = initalState.*succ
}

fact connected {
	all s1: State, s2: State | s1 in s2.*succ
}


pred example {}

run example for exactly 1 StateMachine, 4 State
