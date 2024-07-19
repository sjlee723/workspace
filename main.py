import threading
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data_link_test')))

from data_link_test.modules.model.was_server_test.wasServerModule import WasServerModule
from data_link.modules.model.web_to_was.webToWasModule import WebToWasModule

'''
WAS 서버 실행
'''
def run_was_server():
    was_server_module = WasServerModule()
    was_server_module.run()
    
'''
WEB 서버 실행
'''
def run_web_to_was():
    web_to_was_module = WebToWasModule()
    web_to_was_module.run_scheduler()

'''
스레드, 스케줄러 실행
'''
if __name__ == '__main__':
    # Start WasServerModule in a separate thread
    was_server_thread = threading.Thread(target=run_was_server, daemon=True)
    was_server_thread.start()

    # Start WebToWasModule (blocking)
    web_to_was_module = WebToWasModule()
    web_to_was_module.run_scheduler()


# 이하 도커 테스트용 코드

# import threading
# import argparse
# import os
# import sys
# import time
# from data_link_test.modules.model.was_server_test.wasServerModule import WasServerModule
# from data_link.modules.model.web_to_was.webToWasModule import WebToWasModule

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data_link_test')))

# def run_was_server():
#     was_server_module = WasServerModule()
#     was_server_module.run()

# def run_web_to_was():
#     web_to_was_module = WebToWasModule()
#     web_to_was_module.run_scheduler()

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Start the appropriate server.')
#     parser.add_argument('--role', type=str, required=True, help='Role of the server: web or was')
#     args = parser.parse_args()

#     if args.role == 'was':
#         was_server_thread = threading.Thread(target=run_was_server, daemon=True)
#         was_server_thread.start()

#     elif args.role == 'web':
#         web_to_was_thread = threading.Thread(target=run_web_to_was, daemon=True)
#         web_to_was_thread.start()

#     else:
#         print("Invalid role. Please choose 'web' or 'was'.")

#     # Main thread will wait indefinitely
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Interrupted")


