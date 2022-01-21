//
//  TestView.swift
//  DesignCode
//
//  Created by wangshenghua on 21-3-30.
//

import SwiftUI

struct TestView: View {
    var body: some View {
        VStack(spacing:10) {
            HStack {
                Text("JianDan")
                    .font(/*@START_MENU_TOKEN@*/.title/*@END_MENU_TOKEN@*/)
                    .fontWeight(/*@START_MENU_TOKEN@*/.bold/*@END_MENU_TOKEN@*/)
                Spacer()
                Text("…")
            }
            .padding()
            ScrollView{
                CardViewText()
                CardViewText()
                CardViewText()
                CardViewText()
                CardViewText()
            }

            Spacer()

        }
        
    }
}

struct TestView_Previews: PreviewProvider {
    static var previews: some View {
        TestView()
    }
}

struct CardViewText: View {
    var body: some View {
        VStack{
            Text("Cool")
                .padding(.top)
                .font(.headline)
                .foregroundColor(.black)
            Rectangle()
                .frame(width: 30, height: 3, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                .foregroundColor(.black)
                .opacity(0.2)
                .cornerRadius(/*@START_MENU_TOKEN@*/3.0/*@END_MENU_TOKEN@*/)
                .padding(4)
            HStack {
                Image("Logo2")
                    .padding()
                Text("Highest number of migrant children in border facilities since government started releasing data")
                    .font(.subheadline)
                    .padding(.bottom)
                    .padding(.horizontal,12)
                    .multilineTextAlignment(.leading)
            }
            Divider()
                .opacity(0.2)
            HStack {
                Spacer()
                Text("小咩霸")
                    .font(.footnote)
                    .padding(.top,5)
                    .padding(.bottom,5)
                    .foregroundColor(Color.gray)
            }
            .padding(.horizontal,15)
        }
        .frame(maxWidth:.infinity)
        .background(Color.white)
        .cornerRadius(10)
        .padding(10)
        .padding(.horizontal,10)
        .shadow(radius: 10)
    }
}
