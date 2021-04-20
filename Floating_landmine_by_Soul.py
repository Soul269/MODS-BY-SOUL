#Made By : SOUL 
#My GOOGLE PLAY ID : SOULXGAMING96

import bs
from bsMap import *
import bsMap

def __init__(self, vrOverlayCenterOffset=None):
        """
        Instantiate a map.
        """
        import bsInternal
        bs.Actor.__init__(self)
        self.preloadData = self.preload(onDemand=True)
        
        def path():
                p = bs.newNode('prop', attrs={'position':(-5.750,4.3515026107,2.0),'velocity':(2.0,1.0,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':1.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':1.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bsUtils.animateArray(p,"position",3,{0:(1.830634, 4.830635, 3.830636),10000:(4.8306378, 4.83063588, -6.830639),20000:(-5.422572086, 4.228850685, 2.803988636),25000:(-6.859406739, 4.429165244, -6.588618549),30000:(-6.859406739, 4.429165244, -6.588618549),35000:(3.148493267, 4.429165244, -6.588618549),40000:(1.830377363, 4.228850685, 2.803988636),45000:(-5.422572086, 4.228850685, 2.803988636),50000:(-5.422572086, 4.228850685, 2.803988636),55000:(1.830377363, 4.228850685, 2.803988636),60000:(3.148493267, 4.429165244, -6.588618549),70000:(1.830377363, 4.228850685, 2.803988636),75000:(3.148493267, 4.429165244, -6.588618549),80000:(-5.422572086, 4.228850685, 2.803988636),90000:(-6.859406739, 4.429165244, -6.588618549),95000:(-6.859406739, 4.429165244, -6.588618549)},loop = True)              

        bs.gameTimer(100,bs.Call(path))
        
        # set some defaults
        bsGlobals = bs.getSharedObject('globals')
        # area-of-interest bounds
        aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
        if aoiBounds is None:
            print 'WARNING: no "aoiBounds" found for map:',self.getName()
            aoiBounds = (-1,-1,-1,1,1,1)
        bsGlobals.areaOfInterestBounds = aoiBounds
        # map bounds
        mapBounds = self.getDefBoundBox("levelBounds")
        if mapBounds is None:
            print 'WARNING: no "levelBounds" found for map:',self.getName()
            mapBounds = (-30,-10,-30,30,100,30)
        bsInternal._setMapBounds(mapBounds)
        # shadow ranges
        try: bsGlobals.shadowRange = [
                self.defs.points[v][1] for v in 
                ['shadowLowerBottom','shadowLowerTop',
                 'shadowUpperBottom','shadowUpperTop']]
        except Exception: pass
        # in vr, set a fixed point in space for the overlay to show up at..
        # by default we use the bounds center but allow the map to override it
        center = ((aoiBounds[0]+aoiBounds[3])*0.5,
                  (aoiBounds[1]+aoiBounds[4])*0.5,
                  (aoiBounds[2]+aoiBounds[5])*0.5)
        if vrOverlayCenterOffset is not None:
            center = (center[0]+vrOverlayCenterOffset[0],
                      center[1]+vrOverlayCenterOffset[1],
                      center[2]+vrOverlayCenterOffset[2])
        bsGlobals.vrOverlayCenter = center
        bsGlobals.vrOverlayCenterEnabled = True
        self.spawnPoints = self.getDefPoints("spawn") or [(0,0,0,0,0,0)]
        self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0,0,0,0,0,0)]
        self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                                  or [(0,0,0,0,0,0)])
        self.flagPoints = self.getDefPoints("flag") or [(0,0,0)]
        self.flagPoints = [p[:3] for p in self.flagPoints] # just want points
        self.flagPointDefault = self.getDefPoint("flagDefault") or (0,1,0)
        self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0,0,0)]
        self.powerupSpawnPoints = \
            [p[:3] for p in self.powerupSpawnPoints] # just want points
        self.tntPoints = self.getDefPoints("tnt") or []
        self.tntPoints = [p[:3] for p in self.tntPoints] # just want points
        self.isHockey = False
        self.isFlying = False
        self._nextFFAStartIndex = 0
        
bsMap.Map.__init__ = __init__
