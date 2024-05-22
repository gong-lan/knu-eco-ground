<script>
    import { style } from 'svelte-body';
    import Fa from 'svelte-fa'
    import { faInstagram } from '@fortawesome/free-brands-svg-icons';
    import { Button } from 'bootstrap';

    let lang = false;

    let kor = document.getElementsByClassName("kor");
    let eng = document.getElementsByClassName("eng");

    function change_lang(event) {
        event.preventDefault()
        if(lang == false) {
            lang = true;
        } else {
            lang = false;
        }

        if (lang) {
            for(let i = 0; kor.length - i > 0; i++) {
                kor[i].style.display = "none";
            }
            for(let i = 0; eng.length - i > 0; i++) {
                if(i == 1){
                    eng[i].style.display = "block";
                } else {
                    eng[i].style.display = "inline";
                }
            }
        } else {
            for(let i = 0; kor.length - i > 0; i++) {
                if(i == 1) {
                    kor[i].style.display = "block";
                } else {
                    kor[i].style.display = "inline";
                }
            }
            for(let i = 0; eng.length - i > 0; i++) {
                eng[i].style.display = "none";
            }
        }
    }
</script>

<div class="langSelec">
    <button class="eng langBut" on:click={change_lang}>한국어</button>
    <button class="kor langBut" on:click={change_lang}>English</button>
</div>
<div class="container">
    <h1 style="font-size: 4rem; line-height: 95%" class="logo-kor kor">
        <span class="knu">크누</span>에코<br>그라운드
    </h1>
    <h1 style="font-size: 4rem; line-height: 95%" class="logo-eng eng">
        <span class="knu">KNU</span>ECO<br>GROUND
    </h1>
    <br>
    <br>
    <div class="contents"  style="color: white;">
        <h5 style="font-size: 2rem;">Coming Soon...</h5>
        <br>
        <br>
        <a href="https://www.instagram.com/ecoleaderknu" class="btn btn-primary instagram">
            <Fa icon={faInstagram} /> 
            <span class="kor">인스타그램</span>
            <span class="eng">Instagram</span>
        </a>
    </div>
</div>

<svelte:body use:style={"background-color: black; overflow: hidden;"} />

<style>
    @font-face {
        font-family: 'PartialSansKR-Regular';
        src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-1@1.1/PartialSansKR-Regular.woff2') format('woff2');
        font-weight: normal;
        font-style: normal;
    }
    @font-face {
        font-family: 'Pretendard-Regular';
        src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
        font-weight: 400;
        font-style: normal;
    }
    @font-face {
        font-family: 'ClimateCrisisKR-1979';
        src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2212@1.0/ClimateCrisisKR-1979.woff2') format('woff2');
        font-weight: 900;
        font-style: normal;
    }
    .instagram {
        background: #833ab4;
        background: linear-gradient(
            to right,
            #833ab4,#fd1d1d,#fcb045
        );
        border-color: white
    }
    .logo-kor {
        font-family: 'PartialSansKR-Regular';
        color: #33fc30;
    }
    .logo-eng {
        font-family: 'ClimateCrisisKR-1979';
        color: #33fc30;
    }
    .knu {
        color: #fd1d1d;
    }
    .contents {
        font-family: 'Pretendard-Regular';
    }
    .kor {
        
    }
    .eng {
        display: none;
    }
    .langSelec {
        position: absolute;
        top: 0;
        right: 0;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
    .langSelec .langBut{
        color: white;
        background: none;
        border: none;
    }
</style>