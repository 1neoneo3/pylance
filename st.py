import streamlit as st
from PIL import Image

def main():

    st.title('Pylanceを使ってエラーをスムーズに解決しよう')
    
    st.text('Pythonで自力でエラー解決が解決できるようになるためには、エラー文を読む、\nデバッグをするなどがあります。ただ、コードが長くなればなるほどエラーの解決に時間がかかります。')

    
    st.text('コードが長くなっても、エラー箇所の特定を素早くできるように視覚化して\nくれるのがVSCodeの拡張機能であるPylanceです。')
    
    st.text('ここでは、そのPylanceを使ったエラーの解決方法について紹介していきます。')
    
    st.text('Pylanceの視覚化機能を使うと、自力でエラーを解決する力が早く身に付きます！')

    im('head_img.png', 650)
    
    st.subheader('どのメニューを選びますか？')
    option = st.selectbox(
        '',
        ('Pylanceのインストール方法←まずはこちら！', 'Pylanceによるエラー発見の方法'))
    
    if option == 'Pylanceのインストール方法←まずはこちら！':
        st.subheader('Pylanceのインストール方法')

        st.text('Pylanceをインストールするには、VSCodeの拡張機能でpylanceと入力して、')
        
        im('inst1.png')
        
        st.text('出てきたものをインストールします。')
        im('inst2.png')
        
        st.text('その後に、VSCode右下の歯車ボタンの"管理"をクリック')
        im('kanri.png')
        st.text('"設定"を開きます。')
        im('inst4.png')
        
        st.text('そこで、「python.analysis.typeCheckingMode」を検索して、設定をbasicにします。')
        im('inst5.png')
        
        st.text('これで、Pylanceのインストールが完了です。')

        if st.button('完了したらクリック！'):
            st.text('おめでとうございます！！😆😆')
            im('happy.png', 600)
            st.balloons()
    
    if option == 'Pylanceによるエラー発見の方法':
        st.subheader('Pylanceでのエラーの発見の仕方')

        st.text('Pylanceを入れると下の画像のように、赤い波線が出る箇所があります。\nエラーを発見するには、この赤い部分にカーソルを合わせて見ていきます。')

        im('error.png')
        
        st.subheader('エラー文を選択する')
        option = st.selectbox(
        '',
        ('Expected indented block', 'A is not defined', 'Unexpected indentation', 'Expected ")"', 'Expected expression', 'String literal is unterminated', 'Invalid character in token ""'))
        
        
        if option == 'Expected indented block':
            
            st.subheader('Expected indented block')
            im('expindent.png')

            st.text('この表記が出た場合はインデントをする必要があります。Expectedは「期待されている」という意味です。\nExpected indented blockなので、インデントすることを期待されているという意味になります。')
            
            st.subheader('対処法')
            
            st.text('インデントをするだけ')
            
            st.subheader('このエラーがよく起こる場所')
            st.text('関数の定義、if文、for文、try-except文周りでよく起きます。')
            im('er1.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 600)
                
                st.balloons()           
                
            
        if option == 'A is not defined':
            st.subheader('A is not defined')
            
            im('er2.png')
            st.text('この表記が出た場合はAという変数を定義していない。もしくは、Aというモジュールを\nimportしていないのどちらかです。Aがモジュール名の場合はモジュールのimportの記述\nを忘れている可能性があります。')
            
            st.subheader('対処法')
            
            st.text('import文を忘れている場合はそれを書きます。変数が定義されていない場合は定義します。\n文字に間違いがないかチェックします。')
            
            st.subheader('このエラーがよく起こる場所')
            st.subheader('文字のタイポ')
            st.text('【対処法】→誤字の訂正')
            im('m1.png')
            st.subheader('関数の中の変数')
            st.text('【対処法】→引数として設定してあげる')
            im('m2.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 600)
                
                st.balloons()
                 
                
        if option == 'Unexpected indentation':
            st.subheader('Unexpected indentation')
            
            im('er3.png')
            
            st.text('この表記が出た場合はインデントをする必要がないところでインデントをしている可能性があります。')
            
            im('er4.png')     
            
            st.subheader('対処法')   
            st.text('インデントを解消します。\n例えば上の2つ目のprintだと、if文や、for文、関数の定義のdefの後などではないので\nインデントの必要はないのでインデントを戻します。')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 600)
                
                st.balloons()
                
        if option == 'Expected ")"':
            st.subheader('Expected ")"')
            
            im('er5.png')
            
            st.text('この表記が出た場合は、どこか近くの行で)が抜けている可能性があります。')
            
            st.text('例えば、こちらはprintの最後の)を忘れている例です。')
            im('erim.png')
            
            
            st.subheader('対処法')   
            st.text(')が抜けている箇所を見つけて)を付け足してあげる必要があります。')
            
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 500)
                
                st.balloons()                    

        if option == 'Expected expression':
            st.subheader('Expected expression')
        
            im('er8.png')
            
            st.text('この表記の意味は「式」が期待されています。という意味です。')
            
            st.text('Pythonで「式」とは、実行されることによって何かの結果になるものです。')
            
            st.text('例をあげると、')
            
            st.text('1 + 5')
            
            st.text('[3, 5, 7, 9]')
            
            st.text('など、なんらかの結果やデータになるものが式です。')
            
            st.text('エラーの例としては、例えばこちら')
            im('erim2.png')
            
            st.text('こちらは、)が多いので、本来のprintが式になっていません。')
            
            
            st.subheader('対処法')   
            st.text('式として成立していない部分を見つけて直してあげよう')
            
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 500)
                
                st.balloons() 

        if option == 'String literal is unterminated':
            
            st.subheader('String literal is unterminated')
        
            im('er6.png')
            
            st.text('この表記が出た場合は文字列のクオテーションの閉じ忘れの可能性があります。')
            
            
            
            st.text('例えば、こちらは文字列の最後の"を忘れている例です。')
            im('erim3.png')
            
            
            st.subheader('対処法')   
            st.text('足りていないクオテーションを付け足してあげましょう。')
            
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 500)
                
                st.balloons()      

        if option == 'Invalid character in token ""':
            st.subheader('Invalid character in token ""')
            
            im('er9.png')
            
            st.text('この表記が出た場合、全角の空白が入っている可能性があります。')
            
            st.text('例えば、下ではfor文の:の後ろに全角の空白が入っています。')
            im('erim4.png')
            
            
            st.subheader('対処法')   
            st.text('全角の空白を消します。上のように、文の後に#を置くには「半角スペース2つ分」\n空けて#を置けば問題ないです。')
            
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.text('素晴らしい！！エラー解決の力がまた一つ身に付きました！！😆😆') 
                im('happy.png', 500)
                
                st.balloons()                 
                
                
def im(img, wid=450):
    image = Image.open(img)
    st.image(image, width=wid)

if __name__ == '__main__':
    main()



