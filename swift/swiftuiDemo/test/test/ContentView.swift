//
//  ContentView.swift
//  test
//
//  Created by wangshenghua on 20-10-31.
//

import SwiftUI
import UIKit

struct ContentView: View {
    @State var temperature: Double = 0
    var shoppingList=["no1","no2","no3"]
    var body: some View {
        VStack(alignment: .leading){
            Text("Hello, 咩霸!")
            Text("看小视频 \n看手机 \n被媳妇安排……")
                .font(.subheadline)
                .foregroundColor(.secondary)
            Text(shoppingList[1])
            log(shoppingList[0])
            }
        }
    }

func log(_ log:String) -> EmptyView {
    print("**\(log)")
    return EmptyView()
}

#if DEBUG
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
#endif
