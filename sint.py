import os
import sys
import time
import getpass
import random

# Native Universal ANSI Escape Sequences for Terminal Styling
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
C = "\033[1;36m"  # Cyan
R = "\033[1;31m"  # Red
M = "\033[1;35m"  # Magenta
W = "\033[1;37m"  # White
RESET = "\033[0m"

def clear_screen():
    """Executes a low-level terminal buffer flush to prevent artifact leakage."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.012):
    """Renders data utilizing a synchronous stream writer interface."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def execution_progressbar():
    """Displays a real-time module execution tracking matrix."""
    print(G + "\n[!] SYNCING RESOURCE ROUTINES AND ARCHITECTURE STRATAS...")
    for i in range(0, 101, 10):
        fill = '█' * (i // 5)
        space = '-' * (20 - (i // 5))
        sys.stdout.write(G + f"\r   INTEGRITY CORE LOADING: [{fill}{space}] {i}%")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\n")

def perform_authentication():
    """Manages the generation and evaluation of the randomized coordinate riddle."""
    clear_screen()
    print(G + "╔══════════════════════════════════════════════════════╗")
    print(G + "║               WELCOME TO SEARCH-SINT v1.2            ║")
    print(G + "╚══════════════════════════════════════════════════════╝")
    
    # Required Identity Attribute Capture
    input(G + "\n  ENTER OPERATOR NICKNAME: " + W)
    
    # Numeric Mapping Generation Routine (A=0, B=1 ... Z=25)
    alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_indices = [random.randint(0, 25) for _ in range(4)]
    expected_cipher = "".join([alphabet_string[index] for index in selected_indices])
    coordinate_hint = "-".join([str(index) for index in selected_indices])
    
    print(Y + "  [!] CENTRAL VALIDATION GATE ACTIVE")
    print(G + f"  COORDINATE REFERENCE SEQUENCE: ({coordinate_hint})")
    
    # Captures incoming password buffer without echoing data characters
    captured_credential = getpass.getpass(G + "  ENTER DECRYPTED ACCESS STRING: " + W)
    
    # Evaluates against uppercase transformation and the static override key
    if captured_credential.strip().upper() != expected_cipher and captured_credential.strip() != "MR":
        sys.exit(R + "\n [!] ACCESS VIOLATION DETECTED - MAIN PROCESS TERMINATED\n")
        
    execution_progressbar()

def display_system_header():
    """Renders the standard diagnostic branding banner."""
    banner_graphic = r"""
 ######  ########    ###    ########   ######  ##     ##          ######  #### ##    ## ########
##    ## ##         ## ##   ##     ## ##    ## ##     ##         ##    ##  ##  ###   ##    ##
##       ##        ##   ##  ##     ## ##       ##     ##         ##        ##  ####  ##    ##
 ######  ######   ##     ## ########  ##       ######### #######  ######   ##  ## ## ##    ##
      ## ##       ######### ##   ##   ##       ##     ##               ##  ##  ##  ####    ##
##    ## ##       ##     ## ##    ##  ##    ## ##     ##         ##    ##  ##  ##   ###    ##
 ######  ######## ##     ## ##     ##  ######  ##     ##          ######  #### ##    ##    ##

                                                            .*****############*****.
                                                  .**#**..* *                      .*##**.                                                  
                                             .*#*.       *  *                        * *  .*#*.                                             
                                         .**.           *  **                        #  *      .**.                                         
                                      ***              ..  **                       .#  **         ***                                      
                                   **.                 #    *    .***.  ..****      .*   *            .*#                                   
                                **.                *   *     ******           .#.  .*.   *               .**                                
                             .**                   *.  *       *#*             *****    .*                  **.                             
                           .#.                     **. .*   *   *              #        *   *                 .#.                           
                         .#.                       **.* .*.   .*               *. ..   .*  **                   .#.                         
                       .*.                          .* *.******                 *.  .*** ***.                     .*.                       
                      **                            *..***  *.                   .**** **.**                        **                      
                    **                              . . .*. *         . .        *.  **.***                           **                    
                   #*                                **  ***.                     . *#..  .                            *#                   
                 .*                                    ***   *#**    *  .       .**.#  .**                               *.                 
                **                                      *.     *******  * .**..*.   *.*.                                  **                
               **                                        *.                 *.      *.                                     **               
              **                                          *. *#.    *   *   **.    *.                                       **              
             **                                            *. .**   *   *    *** .*                                          **             
            .*                                            **    **..*   *. *#   **                                            *.            
           .#                                           .* ***  **. **.#*. *.   ***                                            #.           
           *.                                          *. ** .** *.*******.* ****. *                                           .*           
          **                                          *  . *   **.*.     **.#*  *.  *.                                          **          
          *.                                       .*.   .  .   *. ..**.****    *..  .*                                          *          
         **                                    **. .    * .***   **      *.    *  *    ***                                       **         
         *.                               ***     *.*..  ..  . *  .*.....   .*    *    .   **.                                   .*         
         #                          .***     ***    *.    .  .   *.      .*       *     *      ***                                #         
        *#                     *#**         .   .     .   .  *     *...**         *      *         .#*.                           #*        
        **                ***.             *.    *    .   *.*....*        *       *      *              ***                       **        
        *.             **..               ........*   . ..* *   .**      .**     *.       #                 .**.                  .*        
        *.            *.    *             #*      .   .   *      * *    *   ..   #.        *                    *                 .*        
        *.           *.      ..          ...    *##.  . ..#*     .  *  *      * **         *                  . ..                .*        
        *.           *         *         ...      **. .* .*      . ..  .         *          *                 * .*                .*        
        **          #           *       * ..       .**##**       . *   .         *          *                 . .*                **        
        *#         .*            *     ..  .                     . *   *         *     *. ..                 .  .*                #*        
         #         *              *    *   .             ...*..  ...   *        ..       .*                  *  ..                #.        
         *.        *               *   *.  *.****.........*******.*    *        ..          *                .  *.               .*         
         **        *                .**.   **############**********    *        *.            *             .   *                **         
          *        *     ....      .* *    * #####*#*#***********#*    .        *             .             *   *                *          
          **       *         ..   * *  .   . ###*#*******#*#####*#.    ..       *            *             .   *.               **          
           *.      *      .***   *   *  .   .#*****#######*****.**..   ..       *           *              *   *               .*           
           .#      *           *.    ..  .  **############*  **  **.    .      .*           *                 .**              #.           
            .*     *          *       ..   ...#**********##########*    *      ..          *              *   *  *            *.            
             **    *        *.         ..  .. #####***... .....***.     *      *          .*     ..**        .. .*           **             
              **   *       *            .* . .*.#           *   .       *      *          #              *   *  *           **              
               **  *.    *.               *. *  .*          *   *       *      *         *.                 *  .*          **               
                ** .*   *                  *.  . .          .   *       *      *         *              .      ..         **                
                 .*.*  .                    *  *  *         .   *       *     ..        *              ..      *.        *.                 
                   #*                        **   ..         .          *     *        *.              *       *       *#                   
                    **                       *     *         * *        *     *       .*               *       *      **                    
                      **                   .*       *        * *        *     *       *                *       *.   **                      
                       .*.                *.        *.       * *        .     *      *.                *       *. .*.                       
                         .#.            .*           *       * *        .    ..     .*                 *       **#*                         
                           .#.         **             *      ...         .   *      *                  *      .#*                           
                             .**      *               .*      #          .   *     *                   *    **.                             
                                **. **                 ..     #          *   *    .*                   * .**                                
                                   **.                  *     #          *   *    *                   .##                                   
                                      ***                *    *          *   .   *                 ***                                      
                                         .**.             *   .          *  .   .*             .**.                                         
                                             .*#*.         *   .         *  .   *         .*#*.                                             
                                                  .**#**.  ..  *         *  .  ..  .**#**.                                                  
                                                          .*****############*****.

"""
    print(G + banner_graphic)
    print(G + " [ SYSTEM STATUS: OPERATIONAL ]  [ SPEC: ENTERPRISE CONTEXTUAL SEARCH ENGINE ]")
    print(G + " [ CORE AUTHORITY: mrmaestrox ]  [ BUILD DEPLOYMENT: mrmaestrox156-debug ]\n")

def generate_alias_permutation_matrix(name_string):
    """Processes names into exactly 15 modern, context-rich username permutations."""
    sanitized_input = name_string.strip()
    name_segments = sanitized_input.split()
    
    # Establish fallback segments if input is a single term
    primary_segment = name_segments[0] if len(name_segments) > 0 else "user"
    secondary_segment = name_segments[1] if len(name_segments) > 1 else "target"
    
    truncated_primary = primary_segment[:5] if len(primary_segment) > 5 else primary_segment
    
    # Modern identity variation archetypes (gaming, obfuscated, platform-specific)
    permutation_blueprints = [
        f"{primary_segment} _{secondary_segment}",
        f"{truncated_primary}'s _18$6",
        f"{primary_segment}_gamers",
        f"{primary_segment} _elo",
        f"{truncated_primary}'s{secondary_segment}",
        f"{primary_segment}{secondary_segment}",
        f"{primary_segment}_elo",
        f"{primary_segment}.vibe",
        f"its_{primary_segment}{secondary_segment}",
        f"{primary_segment}_specter",
        f"{primary_segment}x0",
        f"the_{primary_segment}_{secondary_segment}",
        f"{primary_segment}_hfx",
        f"alpha_{primary_segment}",
        f"{secondary_segment}_vault"
    ]
    
    # Ensure variations are sanitized and unique
    final_matrix = []
    for item in permutation_blueprints:
        if item not in final_matrix:
            final_matrix.append(item)
            
    # Guarantee exactly 15 records are produced
    while len(final_matrix) < 15:
        final_matrix.append(f"{primary_segment}_node_{random.randint(10,99)}")
        
    return final_matrix[:15]

def execute_runtime_loop():
    """Manages system processes within a structured terminal environment."""
    perform_authentication()
    
    while True:
        clear_screen()
        display_system_header()
        
        type_effect(G + "[1] PLATFORM PROFILE IDENTIFIER LINK GENERATOR (14 CORE ASSETS)")
        type_effect(G + "[2] ADVANCED CONTEXTUAL INTELLIGENCE & FALLBACK SEARCH DIRECTORY")
        type_effect(G + "[3] APPLICATION SHUTDOWN")
        
        selected_option = input(G + "\nSELECT TARGET OPERATIONAL RANGE: " + W).strip()
        
        if selected_option == "1":
            clear_screen()
            display_system_header()
            print(M + "=== ENTRY POINT MODE [01]: CORE TARGET PROFILE ENUMERATION ===")
            raw_target_input = input(G + "INPUT IDENTIFIER OR FULL NAME: " + W).strip()
            
            if not raw_target_input:
                print(R + "[!] INVALID CRITERIA PROVIDED.")
                time.sleep(1.5)
                continue
                
            condensed_target = raw_target_input.replace(" ", "")
            
            # 14 Target platforms deployment array
            target_platforms = {
                "Instagram": "https://www.instagram.com/{}",
                "GitHub Repository": "https://github.com/{}",
                "Twitter / X": "https://twitter.com/{}",
                "Facebook Core": "https://www.facebook.com/{}",
                "TikTok Portal": "https://www.tiktok.com/@{}",
                "Pinterest Index": "https://www.pinterest.com/{}",
                "SoundCloud Audio": "https://soundcloud.com/{}",
                "Behance Portfolio": "https://www.behance.net/{}",
                "Medium Publications": "https://medium.com/@{}",
                "Reddit Forums": "https://www.reddit.com/user/{}",
                "Twitch Streams": "https://www.twitch.tv/{}",
                "LinkedIn Network": "https://www.linkedin.com/in/{}",
                "YouTube Channel": "https://www.youtube.com/@{}",
                "Linktree Assets": "https://linktr.ee/{}"
            }
            
            print(Y + f"\n[+] COMPILING PLATFORM TARGET PROFILE ROUTINES FOR '{raw_target_input}':")
            for platform_title, structure_url in target_platforms.items():
                print(C + f"  [LINK] {platform_title}: {structure_url.format(condensed_target)}")
                
            print(Y + "\n[+] GENERATING 15 COMPLEX MODERN IDENTITY VARIATIONS & ALIASES:")
            calculated_aliases = generate_alias_permutation_matrix(raw_target_input)
            for structural_alias in calculated_aliases:
                print(G + f"  -> Calculated Modern Handle: {structural_alias}")
                
            input(Y + "\n[!] EXECUTION COMPLETED. PRESS ENTER TO CLEAR LAYER AND RE-ISOLATE MENU...")
            
        elif selected_option == "2":
            clear_screen()
            display_system_header()
            print(M + "=== ENTRY POINT MODE [02]: DEEP INTEL & CONTEXTUAL LOOKUP MATRIX ===")
            raw_search_input = input(G + "INPUT COMPREHENSIVE NAME (ANY CASE MIX): " + W).strip()
            
            if not raw_search_input:
                print(R + "[!] INVALID TARGET MATRIX PARAMETER.")
                time.sleep(1.5)
                continue
                
            formatted_url_string = raw_search_input.upper().replace(" ", "+")
            
            print(Y + f"\n[+] COMPILING 16 COMPLEX SPECIFIC IN-DEPTH OPERATOR CORRELATIONS:")
            
            # High-fidelity search parameters matching modern tracking landscapes
            advanced_operator_matrix = [
                ("Global News Mention Archive", f"https://www.google.com/search?q=%22{formatted_url_string}%22+news"),
                ("Social Network Content Tracker", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:reddit.com+OR+site:quora.com"),
                ("Official Public Gazette Directories", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:gov.br"),
                ("Indexed Document Objects (.PDF/.DOC)", f"https://www.google.com/search?q=%22{formatted_url_string}%22+filetype:pdf+OR+filetype:doc"),
                ("Legal Registry Cases & Arbitrations", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:jusbrasil.com.br"),
                ("Instagram Mentions & Public Tags", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:instagram.com"),
                ("LinkedIn Executive Identity Maps", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:linkedin.com/in/"),
                ("Pastebin & Public Leak Trackers", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:pastebin.com+OR+site:controlc.com"),
                ("Engineering Repositories & Commits", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:github.com+OR+site:gitlab.com"),
                ("Self-Published Log Platforms", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:blogspot.com+OR+site:wordpress.com"),
                ("Visual Media Databases", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:flickr.com+OR+site:pinterest.com"),
                ("Academic Index Citation Networks", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:scholar.google.com"),
                ("Corporate Registrars & CNPJ Boards", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:transparencia.cc+OR+site:cnpj.biz"),
                ("Video Stream & Broadcast Outlets", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:youtube.com+OR+site:vimeo.com"),
                ("Recent Temporal Indexing (24h)", f"https://www.google.com/search?q=%22{formatted_url_string}%22&tbs=qdr:d"),
                ("Archived Web Data Mirror Search", f"https://www.google.com/search?q=%22{formatted_url_string}%22+site:archive.org")
            ]
            
            for index_tag, url_path in advanced_operator_matrix:
                print(C + f"  [OPERATOR] {index_tag}:")
                print(W + f"    -> {url_path}")
                
            print(Y + "\n[+] EXTERNAL OSINT ENGINES & COMPLEMENTARY CROSS-REFERENCE DIRECTORY:")
            print(W + "  [!] Copy and run these tools manually if broader coverage is required:")
            
            # Directory of standard alternative fallback lookups
            external_intelligence_directories = [
                "OSINT Framework Comprehensive Aggregator: https://osintframework.com",
                "Wayback Historical Machine Search Engine: https://web.archive.org",
                "DuckDuckGo Privacy Matrix Endpoint:      https://duckduckgo.com",
                "StartPage Decentralized Proxy Portal:    https://www.startpage.com",
                "TinEye Advanced Reverse Image Repository: https://tineye.com"
            ]
            
            for utility_path in external_intelligence_directories:
                print(G + f"   - {utility_path}")
                
            input(Y + "\n[!] EXECUTION COMPLETED. PRESS ENTER TO CLEAR LAYER AND RE-ISOLATE MENU...")
            
        elif selected_option == "3":
            clear_screen()
            print(G + "[!] CLOSING APPLICATION SYSTEM SPACE... STANDBY.")
            sys.exit(0)

if __name__ == "__main__":
    try:
        execute_runtime_loop()
    except KeyboardInterrupt:
        print(R + "\n\n[!] RUNTIME TERMINATION INTERRUPTED VIA USER TERMINAL SIGNAL.")
        sys.exit(0)
