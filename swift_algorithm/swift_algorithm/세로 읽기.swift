
import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    var stringArray: [String] = my_string.map { String( $0 )}
    return stride(from: c - 1, to:my_string.count, by: m).map { stringArray[$0] }.joined()
}
