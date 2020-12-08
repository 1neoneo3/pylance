import streamlit as st
from PIL import Image

def main():

    st.title('Pylanceを使ってエラーをスムーズに解決しよう')
    
    st.markdown('Pythonで自力でエラー解決が解決できるようになるためには、エラー文を読む、デバッグをするなどがあります。ただ、数百行のコードのエラー箇所の特定には時間がかかります。')  
    
    st.markdown('エラー箇所の特定を素早くできるように視覚化してくれるのがVSCodeの拡張機能の**Pylance**です。')   
    
    st.markdown('ここでは、そのPylanceを使ったエラーの解決方法について紹介していきます。')

    im('img/head_img.png')
    
    st.subheader('どのメニューを選びますか？')
    option = st.selectbox(
        '',
        ('Pylanceのインストール方法←まずはこちら！', 'Pylanceによるエラー発見の方法'))
    
    if option == 'Pylanceのインストール方法←まずはこちら！':
        st.subheader('Pylanceのインストール方法')

        st.markdown('Pylanceをインストールするには、VSCodeの拡張機能でpylanceと入力して、')
        
        im('img/inst1.png')
        
        st.markdown('出てきたものをインストールします。')
        im('img/inst2.png')
        
        st.markdown('その後に、VSCode右下の歯車ボタンの"管理"をクリック')
        im('img/kanri.png')
        st.markdown('"設定"を開きます。')
        im('img/inst4.png')
        
        st.markdown('そこで、「**python.analysis.typeCheckingMode**」を検索して、設定を**basic**にします。')
        im('img/inst5.png')
        
        st.markdown('これで、Pylanceのインストールが完了です。')

        if st.button('完了したらクリック！'):
            st.markdown('おめでとうございます！！😆😆')
            im('img/happy.png')
            st.balloons()
    
    if option == 'Pylanceによるエラー発見の方法':
        st.subheader('Pylanceでのエラーの発見の仕方')

        st.markdown('Pylanceを入れると下の画像のように、赤い波線が出る箇所があります。エラーを発見するには、この赤い波線にカーソルを合わせて見ていきます。')

        im('img/error.png')
        
        st.subheader('解決したいエラー文を選択する')
        option = st.selectbox(
        '',
        ('Expected indented block', 'A is not defined', 'Unexpected indentation', 'Expected ")"', 'Expected expression', 'String literal is unterminated', 'Invalid character in token ""', 'Expected ":"', 'A is possibly unbound'))
        
        
        if option == 'Expected indented block':
            
            st.subheader('Expected indented block')
            im('img/expindent.png')

            st.markdown('この表記が出た場合は**インデントをできていない箇所**があります。Expectedは「期待されている」という意味です。Expected indented blockなので、**インデントすることを期待されている**という意味になります。')
            
            st.markdown('例えば次の例だと、if文の後のprint文がインデントされていません。')
            
            im('img/erim6.png')

            st.subheader('対処法')
            
            st.markdown('インデントを忘れている部分があるのでそこをインデントしてあげます。')
            
            im('img/erim7.png')
            
            st.subheader('このエラーがよく起こる場所')
            st.markdown('関数の定義、if文、for文、try-except文周りでよく起きます。')
            
            im('img/er1.png')
            st.markdown('このエラーが出た場合は、それらの文の周りを見直してみましょう。')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/happy.png')
                
                st.balloons()           
                
            
        if option == 'A is not defined':
            st.subheader('A is not defined')
            
            im('img/er2.png')
            st.markdown('この表記が出た場合は**Aという変数を定義していない。**もしくは、**Aというモジュールをimportしていない**のどちらかです。Aがモジュール名の場合はモジュールのimportの記述を忘れている可能性があります。')
            
            st.subheader('対処法')
            st.markdown('次の3つを確認してみて下さい。')
            st.markdown('**①import文を忘れている場合はそれを書きます。**')
            st.markdown('**②変数が定義されていない場合は定義します。**')
            st.markdown('**③文字に間違いがないかチェックします。**')
            
            st.subheader('このエラーがよく起こる場面')

            st.subheader('変数の未定義')
            im('img/meri1.png')
            st.markdown('上の例ではtestという変数が定義されていません。')
            
            st.markdown('【対処法】→手前で変数を定義する。')
            
            im('img/meri2.png')        
            
            st.subheader('文字のタイポ')
            im('img/m1.png')
            
            st.markdown('上の例ではprintと書くところをprntと書いてしまっています。')
            
            st.markdown('【対処法】→誤字の訂正')
            
            st.subheader('関数の中の変数')
            
            im('img/m2.png')
            st.markdown('上の例ではinitialが関数の中で初めて出てきた形になっていて、エラーになっています。')
            st.markdown('【対処法】→引数として設定してあげる')
            
            im('img/emm.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/beach.jpg')
                
                st.balloons()
                
        if option == 'Unexpected indentation':
            st.subheader('Unexpected indentation')
            
            im('img/er3.png')
            
            st.markdown('この表記が出た場合はインデントをする必要がないところでインデントをしている可能性があります。')
            
            im('img/er4.png')     
            
            st.subheader('対処法')   
            st.markdown('インデントを解消します。例えば上の2つ目のprintだと、if文や、for文、関数の定義のdefの後などではなく、インデントの必要はないのでインデントを戻します。')
            
            im('img/er5.png')   
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/happy.png')
                
                st.balloons()
                
        if option == 'Expected ")"':
            st.subheader('Expected ")"')
            
            im('img/mml1.png')
            
            st.markdown('この表記が出た場合は、どこか近くの行で**)が抜けている**可能性があります。')
            
            st.markdown('例えば、こちら↓はfor文の下のprintの最後の)を忘れている例です。')
            im('img/erim.png')
            
            st.subheader('対処法')   
            st.markdown(')が抜けている箇所を見つけて)を付け足してあげる必要があります。')
            
            im('img/elm1.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/smile.jpg')
                
                st.balloons()                    

        if option == 'Expected expression':
            st.subheader('Expected expression')
        
            im('img/er8.png')
            
            st.markdown('この表記の意味は**「式」が期待されています。**という意味です。')
            
            st.markdown('Pythonで「式」とは、実行されることによって何かの結果になるものです。')
            
            st.markdown('例をあげると、')
            
            st.markdown('1 + 5')
            
            st.markdown('[3, 5, 7, 9]')
            
            st.markdown('など、なんらかの結果やデータになるものが式です。')
            
            st.markdown('エラーの例としては、例えばこちら')
            im('img/erim2.png')
            
            st.markdown('1 + 2 + だと式として完成していないのでエラーとなります。')
            
            
            st.subheader('対処法')   
            st.markdown('式として成立していない部分を見つけて直してあげよう')
            
            im('img/erml.png')
            
            st.markdown('5を足すことで一つの式となりました。')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/banzai.png')
                
                st.balloons() 

        if option == 'String literal is unterminated':
            
            st.subheader('String literal is unterminated')
        
            im('img/er6.png')
            
            st.markdown('この表記が出た場合は文字列の**クオテーションの閉じ忘れ**の可能性があります。')
            
            
            
            st.markdown('例えば、こちらは文字列の最後の"を忘れている例です。')
            im('img/erim3.png')
            
            
            st.subheader('対処法')   
            st.markdown('足りていないクオテーションを付け足してあげましょう。')
            
            im('img/errm.png')
            
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！😆😆') 
                im('img/jumping.jpg')
                
                st.balloons()      

        if option == 'Invalid character in token ""':
            st.subheader('Invalid character in token ""')
            
            im('img/er9.png')
            
            st.markdown('この表記が出た場合、**全角の空白**がどこかに入っている可能性があります。')
            
            st.markdown('例えば、下ではfor文の:の後ろに全角の空白が入っています。')
            im('img/erim4.png')
            
            
            st.subheader('対処法')   
            st.markdown(':の後に入っている全角の空白を消します。上のように、文の後に#を置くには「半角スペース2つ分」空けて#を置けば問題ないです。')
            
            im('img/6em.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！一つレベルアップしました😆😆') 
                im('img/jump.jpg')
                
                st.balloons() 
                
        if option == 'Expected ":"':
            st.subheader('Expected ":"')
            
            im('img/ex1.png')
            
            st.markdown('この表記が出た場合、どこかにコロン:を忘れています。')
            
            st.markdown('例えば、下では関数を定義する際のコロン:を忘れています。')
            im('img/ex2.png')
            
            
            st.subheader('対処法')   
            st.markdown('コロン:を忘れている部分に付け足してあげます。')
            
            im('img/ex3.png')
            
            st.markdown('このエラーがよく起こる場面')
            st.markdown('関数の定義、if文、for文、try-except文周りでよく起きます。')
            
            im('img/er1.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！一つレベルアップしました😆😆') 
                im('img/happy.png')
                
                st.balloons()
            
        if option == 'A is possibly unbound':
            st.subheader('A is possibly unbound')
            
            im('img/unbound.png')
            
            st.markdown('この表記が出た場合、変数Aが未定義になっている可能性があります。')
            
            st.markdown('例えば、下ではinfo_dictはtry文が実行された時だけ定義されて、exceptの時は定義されていません。ですのでexcept文が実行された時はinfo_dictが定義されていないとエラーが出ます。')
            im('img/unbound2.png')
            
            
            st.subheader('対処法')   
            st.markdown('info_dictをtry、exceptのどちらの場合でも定義されるような場所で定義してあげる。')
            
            im('img/unbound3.png')
            
            st.subheader('エラーは解消できましたか？')
            if st.button('赤い波線が消えたらクリック'):
                st.markdown('素晴らしい！！エラー解決の力がまた一つ身に付きましたね！！一つレベルアップしました😆😆') 
                im('img/gutts.jpg')
                
                st.balloons()                      
                
                
def im(img, wid=700):
    image = Image.open(img)
    st.image(image, width=wid)

if __name__ == '__main__':
    main()
