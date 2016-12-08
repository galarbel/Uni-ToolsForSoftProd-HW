sig Person {
    father: lone Person,
    mother: lone Person
}

fact { all p: Person | p.father != p.mother }

pred parent(p1: Person, p2:Person) {
    p1 = p2.father or
    p1 = p2.mother
}

//run parent for 5


fact { all p: Person | !parent[p , p] }
fact { all p1, p2: Person | ! (parent[p1 , p2] and parent[p2, p1] ) }

pred show () {}

fun grands (p: Person): set Person {
    p.(father+mother).(father+mother)
}

fact { no p: Person |  p in grands[p] }

assert sibsNotParents {
    no p1, p2: Person | 
        some p3: Person | 
            parent[p3, p1] and parent[p3, p2] and parent[p1, p2] and p1 != p2
}

//run show for 5

check sibsNotParents for 5
