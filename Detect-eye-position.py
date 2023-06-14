import cv2
import mediapipe as mp

try:
    # MediaPipe Face Mesh初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    # カメラ初期化
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("カメラが見つかりません。")
        exit()

    while True:
        success, image = cap.read()
        if not success:
            print("カメラから画像を取得できませんでした。")
            break
        
        # 画像をRGBに変換
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 顔のランドマークを検出
        results = face_mesh.process(image)
        
        # 画像をBGRに戻す
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # 顔のランドマークを描画
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 左目のランドマークインデックス
                left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155]
                # 右目のランドマークインデックス
                right_eye_indices = [263, 249, 390, 373, 374, 380, 381, 382]
                
                left_eye_x = sum(face_landmarks.landmark[i].x for i in left_eye_indices) / len(left_eye_indices)
                left_eye_y = sum(face_landmarks.landmark[i].y for i in left_eye_indices) / len(left_eye_indices)
                
                right_eye_x = sum(face_landmarks.landmark[i].x for i in right_eye_indices) / len(right_eye_indices)
                right_eye_y = sum(face_landmarks.landmark[i].y for i in right_eye_indices) / len(right_eye_indices)

                # 画面上の座標に変換
                ih, iw, _ = image.shape
                left_eye_x, left_eye_y = int(left_eye_x * iw), int(left_eye_y * ih)
                right_eye_x, right_eye_y = int(right_eye_x * iw), int(right_eye_y * ih)

                # 目の中心に円を描く
                cv2.circle(image, (left_eye_x, left_eye_y), 5, (0, 255, 0), -1)
                cv2.circle(image, (right_eye_x, right_eye_y), 5, (0, 255, 0), -1)
                
        # 画像を表示
        cv2.imshow('MediaPipe FaceMesh', image)
        
        # 'q'キーで終了
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()
