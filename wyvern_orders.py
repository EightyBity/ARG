import sys
import time
import getpass
import newuserdesktop

import cls

def wyvernOrders():
    cls.cls()
    warning = '''a password is required to continue, be careful it is case sensitive
'''
    incorrect = 0
    for characters in warning:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
        
    while True:
        password = getpass.getpass('Password:') 

        if password != 'HATDIE' and incorrect < 3:
            incorrect+=1
            cls.cls()
            wrong = '''Wrong password please try again
'''
            for characters in wrong:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
        elif password == 'HATDIE':
            cls.cls()
            correct = 'Password accepted'
            time.sleep(1)
            wyvernOrdersText()
            for characters in correct:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
        elif incorrect == 3:
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
def wyvernOrdersText():
    cls.cls()
    print('''________________________________________________________________________________________________________________________________________''')
    orders = '''
codename: last resort

Wyvern 3, this file is to be hidden and protected by password on the project Overall Situation.
This is not to be used to hide or use any other passwords and should only be used for the last resort orders.
These orders will take effect in the case that I am captured and/or terminated at the ceremony of the delta foxes.

Wyvern 2 will get the mantle of Wyvern lead 1 and thus shall get the powers required to him in this instance.

Wyvern 3 will hence be upgraded to wyvern 2 and will keep his current powers.

The project Overall Situation must be brought to term as soon as feasibly possible.

To all the remaining Wyverns, this message will need to be made public

"My fellow wyverns, it is with a heavy heart I announce today the loss of Wyvern 1, he has been taken/terminated in the line of duty.
In his final moments, Wyvern 1 still wanted to tell you how proud he was to ever fly with you, and how proud he was to look back at
the squadron that grew so much more than he anticipated. He will be forever missed in the 108th Wyvern squadron. Effective immediately,
Wyvern 2 will be taking the lead, listen to him as such you would Wyvern 1. Fly high

Wyvern lead 1"
___________________________________________________________________________________________________________________________________________

write back to go back

'''
    for characters in orders:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.05)
    while True:
        player = input()
        if player.lower().strip() == 'back':
            newuserdesktop.userScreen()
        else:
            cls.cls()
            print('''________________________________________________________________________________________________________________________________________

codename: last resort

Wyvern 3, this file is to be hidden and protected by password on the project Overall Situation.
This is not to be used to hide or use any other passwords and should only be used for the last resort orders.
These orders will take effect in the case that I am captured and/or terminated at the ceremony of the delta foxes.

Wyvern 2 will get the mantle of Wyvern lead 1 and thus shall get the powers required to him in this instance.

Wyvern 3 will hence be upgraded to wyvern 2 and will keep his current powers.

The project Overall Situation must be brought to term as soon as feasibly possible.

To all the remaining Wyverns, this message will need to be made public

"My fellow wyverns, it is with a heavy heart I announce today the loss of Wyvern 1, he has been taken/terminated in the line of duty.
In his final moments, Wyvern 1 still wanted to tell you how proud he was to ever fly with you, and how proud he was to look back at
the squadron that grew so much more than he anticipated. He will be forever missed in the 108th Wyvern squadron. Effective immediately,
Wyvern 2 will be taking the lead, listen to him as such you would Wyvern 1. Fly high

Wyvern lead 1"
___________________________________________________________________________________________________________________________________________

I didnt get that please make sure to write back to go back
''')    
if __name__ == '__main__':
    wyvernOrders()