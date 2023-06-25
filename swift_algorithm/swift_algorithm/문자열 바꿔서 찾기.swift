
import Foundation

func ssdolution(_ myString:String, _ pat:String) -> Int {
    return myString.map { $0 == "A" ? "B" : "A" }.joined().contains(pat) ? 1 : 0
}
