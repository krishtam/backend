from sqlalchemy.orm import Session
from models.progress import Progress
from schemas.progress import ProgressBase

def update_progress(db: Session, progress_data: ProgressBase):
    progress = db.query(Progress).filter(
        Progress.user_id == progress_data.user_id,
        Progress.unit_id == progress_data.unit_id
    ).first()
    
    if progress:
        progress.progress_percentage = progress_data.progress_percentage
    else:
        progress = Progress(**progress_data.dict())
        db.add(progress)
    
    db.commit()
    db.refresh(progress)
    return progress
