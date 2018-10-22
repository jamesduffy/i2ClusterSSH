# -*- mode: python -*-

block_cipher = None


a = Analysis(['i2ClusterSSH.py'],
             pathex=['/Users/jamesduffy/Projects/i2ClusterSSH'],
             binaries=[],
             datas=[],
             hiddenimports=['configparser'],
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
          name='i2ClusterSSH',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
