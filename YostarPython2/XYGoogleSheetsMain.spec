# -*- mode: python -*-

block_cipher = None


a = Analysis(['XYGoogleSheetsMain.py'],
             pathex=['/Users/yostar/YostarPython2'],
             binaries=[],
             datas=[('/Users/yostar/YostarPython/credentials.json', 'YostarPython/credentials.json')],
             hiddenimports=['requests', '__future__', 'pickle', 'googleapiclient.discovery', 'google_auth_oauthlib.flow', 'google.auth.transport.requests'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Yo-StarMediaListDatabase',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
