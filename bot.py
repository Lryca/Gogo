import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import os


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("식사")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")



    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot and message.content=="오빠 나 건들지마.":
            channel=message.channel
            msg="힝.."
            await channel.send(msg)
            return None
            
        if message.author.bot:
            return None

        if message.content=="?홀" or message.content=="?짝":
            global num
            num=random.randint(1,100)
            channel=message.channel
            
            if message.content=="?홀":
                channel=message.channel
                if num%2==0:
                    await channel.send("그것도 못 맞추세요? ")
                    await channel.send(num)
                    return None
                elif num%2==1:
                    await channel.send("우와 대단해요!")
                    await channel.send(num)
                    return  None
            if message.content=="?짝":
                channel=message.channel
                if num%2==0:
                    await channel.send("우와 대단해요!")
                    await channel.send(num)
                    return None
                if num%2==1:
                    await channel.send("그것도 못 맞추세요?")
                    await channel.send(num)
                    return  None
                
        if message.content == "고고야 홀짝할래?":
             channel = message.channel
             num=random.randint(1,2)
             if num==1:
                 asw="도박은 안 좋은 거에요냥"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="준비"
                 await channel.send(asw)
                 return None

                
        # message.content = message의 내용
        if message.content == "고고야 바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "너도 바보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
            
        if message.content == "고고야 산책할래?":
             channel = message.channel
             asw="오늘은 쉴래요냥"
             await channel.send(asw)
             return None

        if message.content == "고고야 고구마":
             channel = message.channel
             asw="갑자기요?"
             await channel.send(asw)
             return None

        if message.content == "ㅠ":
             channel = message.channel
             asw="모야 울지마요"
             await channel.send(asw)
             return None

        if message.content == "고고야 놀자":
             channel = message.channel
             asw="(무시)"
             await channel.send(asw)
             return None
            
        if message.content == "고고야 안녕":
             channel = message.channel
             asw="안냥냥."
             await channel.send(asw)
             return None

        if message.content == "고고야 씻자":
             channel = message.channel
             asw="캬아아악!!!"
             await channel.send(asw)
             return None

        if message.content == "고고야 고등어":
             channel = message.channel
             num=random.randint(1,4)
             if num==1:
                 asw="저..전 그런걸로 안넘어가요!"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="당신도 오늘 고등어 한 마리 어때요?"
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="고등어는 언제 먹어도 맛있어요."
                 await channel.send(asw)
                 return None
             if num==4:
                 asw="제가 세상에서 가장 좋아하는 물고기랍니다!"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 츄르":
             channel = message.channel
             asw="넘나 좋아요 냥!!"
             await channel.send(asw)
             return None
            
        if message.content == "고고 싫어" or message.content =="고고 미워":
             channel = message.channel
             num=random.randint(1,4)
             if num==1:
                 asw="나도 너 싫다냥"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="제가 뭘 잘못 했냐요?"
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="?뭐냥 시비거는거냥?"
                 await channel.send(asw)
                 return None
             if num==4:
                 asw="제 귀여움이 질투 나는 거냐옹?"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 밥먹자":
             channel = message.channel
             asw="고등어가 좋을 것 같아요."
             await channel.send(asw)
             return None

        if message.content == "나가":
             channel = message.channel
             asw="ㅗ"
             await channel.send(asw)
             return None


        if message.content == "고고야 대학 싫어":
             channel = message.channel
             asw="자퇴하세냥"
             await channel.send(asw)
             return None

        if message.content == "고고야 교수님이 미워":
             channel = message.channel
             num=random.randint(1,3)
             if num==1 :
                 asw="드랍하세냥"
                 await channel.send(asw)
                 return None
             if num==2 :
                 asw="자퇴하세냥"
                 await channel.send(asw)
                 return None
             if num==1 :
                 asw="제 고등어 드릴게요.. 힘내세요!"
                 await channel.send(asw)
                 return None  

        if message.content == "고고야 츄르 압수":
             channel = message.channel
             asw="으으우으우에에엥"
             await channel.send(asw)
             return None

        if message.content == "팍씨":
             channel = message.channel
             num=random.randint(1,3)
             if num==1:
                 asw="뭐이씨"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="히잉 고고 그만 괴롭혀요.."
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="ㅋ"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 칭찬" or message.content == "고고야 나 잘했지?":
             channel = message.channel
             await channel.send(" 참 잘했어요!")
             return None

        if message.content == "고고야 귀여워"or message.content == "고고 귀여워":
            channel = message.channel
            num=random.randint(1,4)
            if num==1:
                asw="그걸 말하는 당신이 더 귀여울지도 몰라요"
                await channel.send(asw)
                return None
            if num==2:
                asw="제가 좀 귀엽긴해요"
                await channel.send(asw)
                return None
            if num==3:
                asw="그걸 이제 아셨군요!"
                await channel.send(asw)
                return None
            if num==4:
                await message.add_reaction("❤️")
                return None

        if message.content == "고고야 미안해":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="저도 미안해요..."
                await channel.send(asw)
                return None
            if num==2:
                asw="그 사과 받아주겠어요냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="앞으로도 사이좋게 지내요 냥"
                await channel.send(asw)
                return None

        if message.content == "고고야 행복하면 야옹해" or message.content == "고고 행복하면 야옹해":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="야옹!"
                await channel.send(asw)
                return None
            if num==2:
                asw="옹냐"
                await channel.send(asw)
                return None
            if num==3:
                asw="(꼬리를 탁탁 치고있다.)"
                await channel.send(asw)
                return None

        if message.content == "고고야 우리 집에 올래?" or message.content=="고고야 우리집에 올래?" or message.content=="고고야 우리집 올래?" or message.content=="고고야 우리 집 올래?" :
            channel = message.channel
            num=random.randint(1,6)
            if num==1:
                asw="좋아요냥!"
                await channel.send(asw)
                return None
            if num==2:
                asw="에...싫은데..."
                await channel.send(asw)
                return None
            if num==3:
                asw="마음이 내키면 갈게요냥"
                await channel.send(asw)
                return None
            if num==4:
                asw="싫어요 안돼요 하지마세요"
                await channel.send(asw)
                return None
            if num==5:
                asw="제가 좀 바빠서요"
                await channel.send(asw)
                return None
            if num==6:
                asw="리리가 한가해 보이던데요?"
                await channel.send(asw)
                return None
            if num==7:
                asw="유유가 할 짓이 없대요."
                await channel.send(asw)
                return None


        if message.content == "고고야 손" or message.content == "냥발" :
             channel = message.channel
             num=random.randint(1,3)
             if num==1 :
                 asw="(멀뚱거리며 당신을 바라보고 있다.)"
                 await channel.send(asw)
                 return None

             if num==2 :
                 asw="(꼬리를 슬며시 들어올려 건넨다)"
                 await channel.send(asw)
                 return None
             if num==3 :
                 asw="냥발 냥!"
                 await channel.send(asw)
                 return None

        if message.content == "?":
             channel = message.channel
             asw="?"
             await channel.send(asw)
             return None

        if message.content == "뀨":
             channel = message.channel
             asw="뀨뀨냥"
             await channel.send(asw)
             return None

        if message.content == "!":
             channel = message.channel
             asw="!!"
             await channel.send(asw)
             return None


        if message.content == "고고야 돈줘" or message.content == "돈줘":
             channel = message.channel
             asw="고양이한테 뭘 바라는거죠?"
             await channel.send(asw)
             return None

        if message.content == "고고야 나가" or message.content == "고고야 저리가":
             channel = message.channel
             asw="니가 가"
             await channel.send(asw)
             return None
            
        if message.content == "고고야 사랑해":
            channel = message.channel
            num=random.randint(1,5)
            if num==1:
                asw="저도 사랑해요냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="저는 아닌데요?"
                await channel.send(asw)
                return None
            if num==3:
                asw="고등어 주면 저도 사랑할수도.."
                await channel.send(asw)
                return None
            if num==4:
                asw="(살짝 거리를 둔다.)"
                await channel.send(asw)
                return None
            if num==5:
                await channel.send("조금 사랑해요")
                return None


        if message.content == "야":
             channel = message.channel
             num=random.randint(1,2)
             if num==1:
                 asw="뭐"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="(무시)"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 아파":
             channel = message.channel
             num=random.randint(1,2)
             if num==1:
                 asw="호~ 해드릴게요. 호오~"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="아프지마요ㅠ 츄르 줄 사람 없어요 냥"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 힘들어":
             channel = message.channel
             num=random.randint(1,5)
             if num==1:
                 asw="주무시는걸 추천드려요."
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="저는 안 힘든데요?"
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="저랑 계속 이야기 하다보면 힘든 일을 잊을 수 있으실 거에요."
                 await channel.send(asw)
                 return None
             if num==4:
                 asw="맛있는 거라도 먹으시는거 어때요? 저는 힘들때마다 고등어를 먹어요."
                 await channel.send(asw)
                 return None
             if num==5:
                 asw="제가 노래라도 불러드릴까요? '고고야 노래' 라고 치시면 제가 노래를 해드릴게요."
                 await channel.send(asw)
                 return None

        if message.content == "고고야 살려줘":
             channel = message.channel
             num=random.randint(1,3)
             if num==1:
                 asw="네? 이..일단 제 손을 잡으세요!"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="항상 안타까운 현실은 찾아오는 법이죠."
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="무슨 일 있으세요? 제가 들어드릴게요."
                 await channel.send(asw)
                 return None

        if message.content == "고고야 리리는 뭐해?":
             channel = message.channel
             num=random.randint(1,3)
             if num==1:
                 asw="몰라요. 요즘 좀 컷다고 오빠한테 말도 안해요"
                 await channel.send(asw)
                 return None
             if num==2:
                 asw="낚시하고 있어요"
                 await channel.send(asw)
                 return None
             if num==3:
                 asw="잠자리채를 휘두르고 있어요"
                 await channel.send(asw)
                 return None

        if message.content == "고고야 리리가 누구야?":
             channel = message.channel
             asw="오빠한테 까부는 말썽꾸러기 동생이에요. 어렸을 땐 귀여웠는데요......."
             await channel.send(asw)
             return None

        if message.content == "고고야 유유가 누구야?":
             channel = message.channel
             asw="맨날 책만 보는 못말리는 남동생이에요... 최근에는 추리물에 빠진 것 같아요"
             await channel.send(asw)
             return None

        if message.content == "고고야 노래":
             channel = message.channel
             asw="노래 할 기분이 아니에요."
             await channel.send(asw)
             return None


        if message.content == "고고야 잘있어":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="오늘도 즐거웠어요냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="내일도 즐거운 하루 되세요냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="조금 더 있다 가면 안돼요냥..?"
                await channel.send(asw)
                return None

        if message.content == "ㅋ":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="재밌으세요?"
                await channel.send(asw)
                return None
            if num==2:
                asw="ㅋ"
                await channel.send(asw)
                return None
            if num==3:
                asw="절 비웃은건가요?"
                await channel.send(asw)
                return None

        if message.content == "고고야 보고싶어":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="저도 당신이 보고싶어요냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="저는 항상 당신 옆에 있어요."
                await channel.send(asw)
                asw="아..제가 잘 때 빼구요 냥냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="(큰 눈으로 당신을 바라보고있다.)"
                await channel.send(asw)
                return None

        if message.content == "고고야 좋은아침" or message.content == "고고야 좋은 아침" or message.content == "고고야 굿모닝":
            channel = message.channel
            num=random.randint(1,3)
            if num==1:
                asw="오늘 하루도 즐겁게 보내세요냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="굿모냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="당신의 하루를 응원합니다냥"
                await channel.send(asw)
                return None

        if message.content == "고고야 잘자":
            channel = message.channel
            num=random.randint(1,4)
            if num==1:
                asw="오늘 하루는 즐거웠냐요?"
                await channel.send(asw)
                return None
            if num==2:
                asw="안녕히 주무세냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="좋은 꿈 꾸세요냥"
                await channel.send(asw)
                return None
            if num==4:
                asw="악몽꾸세냥"
                await channel.send(asw)
                return None

        if message.content == "고고님"or message.content =="고고야":
            channel = message.channel
            num=random.randint(1,7)
            if num==1:
                asw="야옹!"
                await channel.send(asw)
                return None
            if num==2:
                asw="냥냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="불렀냐요?"
                await channel.send(asw)
                return None
            if num==4:
                asw="(말 없이 그루밍을 하고있다.)"
                await channel.send(asw)
                return None
            if num==5:
                asw="그만 불러요."
                await channel.send(asw)
                return None
            if num==6:
                asw="왜"
                await channel.send(asw)
                return None
            if num==7:
                asw="(^._.^)ﾉ"
                await channel.send(asw)
                return None


        if message.content == "고고야 배고파":
            channel = message.channel
            num=random.randint(1,11)
            if num==1:
                asw="오늘은 라면을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="오늘은 연어를 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="오늘은 김밥을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==4:
                asw="오늘은 마라탕을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==5:
                asw="오늘은 제가 제일 좋아하는 고등어 정식 어떠냐요?"
                await channel.send(asw)
                return None
            if num==6:
                asw="하루쯤 굶어도 나쁘지않을 것 같아요냥"
                await channel.send(asw)
                return None
            if num==7:
                asw="오늘은 초밥을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==8:
                asw="오늘은 짜장면을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==9:
                asw="오늘은 스테이크를 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==10:
                asw="오늘은 치킨을 추천드려요 냥"
                await channel.send(asw)
                return None
            if num==11:
                asw="오늘은 카레를 추천드려요 냥"
                await channel.send(asw)
                return None
            

        if message.content == "고고야 뭐해":
            channel = message.channel
            num=random.randint(1,6)
            if num==1:
                asw="고등어 먹고 있어요냥"
                await channel.send(asw)
                return None
            if num==2:
                asw="산책하고 있어요냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="풀밭에서 뒹굴고 있어요냥"
                await channel.send(asw)
                return None
            if num==4:
                asw="낚시 중 이에요냥"
                await channel.send(asw)
                return None
            if num==5:
                asw="야옹하고 있어요냥"
                await channel.send(asw)
                return None
            if num==6:
                asw="말 그만 거세요냥"
                await channel.send(asw)
                return None
            
        if message.content == "고고야 물어":
            channel = message.channel
            num=random.randint(1,4)
            if num==1:
                asw="크앙!"
                await channel.send(asw)
                return None
            if num==2:
                asw="그 명령에 책임을 질 수 있냐요?"
                await channel.send(asw)
                return None
            if num==3:
                asw="야옹!!!(덥썩)"
                await channel.send(asw)
                return None
            if num==4:
                asw="드디어 제 이빨이 활약할 때가 왔녜요"
                await channel.send(asw)
                return None


        if message.content == "고고야 심심해" or message.content == "심심해":
            channel = message.channel
            num=random.randint(1,4)
            if num==1:
                asw="저랑 놀아요!!"
                await channel.send(asw)
                return None
            if num==2:
                asw="고등어 주면 놀아 드릴게냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="리리한테 가봐요"
                await channel.send(asw)
                return None
            if num==4:
                asw="(무시)"
                await channel.send(asw)
                return None

        if message.content == "고고야 잘한다"or message.content=="고고야 잘했어":
            channel = message.channel
            num=random.randint(1,4)
            if num==1:
                asw="저밖에 없죠?"
                await channel.send(asw)
                return None
            if num==2:
                asw="츄르로 보답해 주세요 냥"
                await channel.send(asw)
                return None
            if num==3:
                asw="냐냥!"
                await channel.send(asw)
                return None
            if num==4:
                asw="어휴 역시 제가 없으면 안 되네요"
                await channel.send(asw)
                return None

        if message.content == "고고야 가위바위보 할래? 가위" or message.content == "고고야 가위바위보 할래? 바위" or message.content == "고고야 가위바위보 할래? 보":
            num= random.randint(1, 3)
        
            if num== 1:    # random 에 저장된 변수가 1일때 (가위 일때)
                if message.content == "고고야 가위바위보 할래? 가위":
                    await message.channel.send("가위!")
                    await message.channel.send("비겼다냥")

                elif message.content == "고고야 가위바위보 할래? 바위":
                    await message.channel.send("가위!")
                    await message.channel.send("히이잉 졌다냥..")

                else:    # 가위도 아니고 바위도 아닌것은 보
                    await message.channel.send("가위!")
                    await message.channel.send("냥! 이겼다 냥!!")

            if num== 2:    # random 에 저장된 변수가 2일때 (바위 일때)
                if message.content == "고고야 가위바위보 할래? 가위":
                    await message.channel.send("바위!")
                    await message.channel.send("냥! 이겼다 냥!!")

                elif message.content == "고고야 가위바위보 할래? 바위":
                    await message.channel.send("바위!")
                    await message.channel.send("비겼다냥")

                else:
                    await message.channel.send("바위!")
                    await message.channel.send("히이잉 졌다냥..")

            if num == 3:    # random 에 저장된 변수가 3일때 (보 일때)
                if message.content == "고고야 가위바위보 할래? 가위":
                    await message.channel.send("보!")
                    await message.channel.send("히이잉 졌다냥..")

                elif message.content == "고고야 가위바위보 할래? 바위":
                    await message.channel.send("보!")
                    await message.channel.send("냥! 이겼다 냥!!")

                else:
                    await message.channel.send("보!")
                    await message.channel.send("비겼다냥")



# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(os.environ['token'])

