# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'ip_watcher.py'],
             pathex=['E:\\workspace\\GitHub\\ip_watcher'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'ip_watcher.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
