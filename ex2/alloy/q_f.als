sig State {
	succ: set State
}

one sig deadlock extends State {
	
}

sig  StateMachine {
	initalState: one State,
	machineReachable: set State
}{
	machineReachable = initalState.*succ
}

fact deadlockNoSucc {
	no deadlock.succ
}

fact deadlockReachable {
	deadlock in StateMachine.machineReachable
}

pred example {}

run example for exactly 1 StateMachine, 4 State
