maya.cmds.polySphere(r=20);
maya.cmds.move( 5, 150, 180 )


def rotate_door():
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_1"+'.ry');
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_2"+'.ry');
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_4"+'.ry');
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_6"+'.ry');  
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_9"+'.ry');   
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_11"+'.ry');   
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_13"+'.ry');       
   
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_3"+'.ry');
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_5"+'.ry'); 
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_7"+'.ry');
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_8"+'.ry');  
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_10"+'.ry');   
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_12"+'.ry');   
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_14"+'.ry');  
   maya.cmds.connectAttr("pSphere1"+'.ry', "cupboard_15"+'.ry'); 
   
   maya.cmds.connectAttr("pSphere1"+'.rz', "drawer_1"+'.tz');

   maya.cmds.connectAttr("pSphere1"+'.rz', "drawer_4"+'.tz');  
   maya.cmds.connectAttr("pSphere1"+'.rz', "drawer_5"+'.tx');   
   maya.cmds.connectAttr("pSphere1"+'.rz', "drawer_6"+'.tx'); 
      
   maya.cmds.select(sphere);

rotate_door()

maya.cmds.multiplyDivide