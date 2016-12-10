sig State {
	succ: set State
}

some sig unReachableFromLock extends State {
	
}

some sig livelock  extends State {

}

sig  StateMachine {
	initalState: one State,
	machineReachable: set State
}{
	machineReachable = initalState.*succ
}

fact unReachableFromLock_is_UnReachableFromLock {
	all s: unReachableFromLock, l: livelock | not s  in l.*succ
}

fact unReachableFromLock_is_ReachableFromMachine {
	unReachableFromLock in StateMachine.machineReachable
}

fact liveLockisInfinite {
	some l1: livelock |  some l2: livelock | l1 in l2.*succ and l2 in l1.*succ
}

pred example {}

run example for exactly 1 StateMachine, 4 State
