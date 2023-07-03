import Foundation

func solution(_ n:Int64) -> Int64 {
    let intNum: Int64 = Int64(sqrt(Double(n)))
    
    return intNum * intNum == n ? (intNum + 1) * (intNum + 1) : -1
}
