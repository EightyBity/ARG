import sys
import time
import getpass

import cls
import newuserdesktop

def wyvern1():
    cls.cls()
    code = '''a password is required
'''
    for characters in code:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
    incorrect = 0
    while True:
        player = getpass.getpass('Password:')
        if player == 'HATDIE':
            cls.cls()

            password = '''SGpncGN5IGFsZGRoemNvZCwgeGZkZSBtcCBweW5jamFlcG8gdHkgbWxkcCA2NCBseW8gYWxkZHBv
IG1qIGwgbmxwZGxjIG56b3AgbnRhc3BjIGV6IG9wbnpvcAoKSGpncGN5IDE6IHl6IGxubnpmeWUK
CkhqZ3BjeSAyOiB5eiBsbm56ZnllCgpIamdwY3kgMzogTnRhc3BjQXdwbGRmY3A=

this message has been encoded

write back to go back

'''
            for character in password:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            while True:
                player = input()
                if player.lower().strip() == 'back':
                    newuserdesktop.userScreen()
                else:
                    cls.cls()
                    print('''SGpncGN5IGFsZGRoemNvZCwgeGZkZSBtcCBweW5jamFlcG8gdHkgbWxkcCA2NCBseW8gYWxkZHBv
IG1qIGwgbmxwZGxjIG56b3AgbnRhc3BjIGV6IG9wbnpvcAoKSGpncGN5IDE6IHl6IGxubnpmeWUK
CkhqZ3BjeSAyOiB5eiBsbm56ZnllCgpIamdwY3kgMzogTnRhc3BjQXdwbGRmY3A=

this message has been encoded

I didnt quite get that please make sure to write back to go back
''')
        elif incorrect < 3:
            cls.cls()
            incorrect+=1
            wrong = '''Wrong password please try again
'''
            for characters in wrong:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
        else:
            cls.cls()
            time.sleep(3)
            giberrish = '''N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM
N<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7
mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.
UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;
l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne
6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>
öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖHWfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZt
z4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)
y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAMN<,F!A>Äbif_3;V3ne6BH3)rY+agYbF+_,xngVSiP+,T,O_-r04gzBG3%Q_Gev<9ÄÖÜYsEkyÄM0CxD2eYgiX*Q-üF)KbY!4!Ü0r7mpgk-
Fp1:4!äqäUHWyz4ÜA1j*cn.L-!Üw!,e?-fmd(rTÄ6Ä%Ch+q3x>öüChnK(wMGgRX-jXÄbäeYääTlyYhJ!of4H+a1G.(oyM7ÜÖzOWx_bRsxx;E;.GBgAÄFW6PdaQsfn.UzÜÖD-vDüC_,NPdÜA3uo?ÖH
Wfn.$3)w,?oÄm&A,*;Yünä?s*zhRJ:10RvhÖl:VZtz4RPzbFB>rbKüCÜj9!bFtjHS2Df(öö9.itFG>i#e(vv&pvWEMPj+c_8z0yj&&L_Bz+;l6fKjdLr-Ei,!3äd.ahXHY)iedl*#+G#y4c>6!Wü#J
)a<jsUS6EeEjgQD,A0_6Wü%WUekE0<21L)y,yl(WY8xX<Z;&u;;DC2ü#7*j_öz0-Eq71HkzSAM'''
            for characters in giberrish:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.0000001)
            newuserdesktop.userScreen()
if __name__ == '__main__':
    wyvern1()