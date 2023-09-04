from fastapi import status, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.vote import Vote
from database_utils import get_db
import models, oauth2

router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: Vote,
    db: Session = Depends(get_db),
    current_user: str = Depends(oauth2.get_current_user),
):
    vote_query = db.query(models.Vote).filter(
        models.Vote.character_id == vote.character_id,
        models.Vote.user_id == current_user.user_id,
    )
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Already voted on this post",
            )
        new_vote = models.Vote(
            character_id=vote.character_id, user_id=current_user.user_id
        )
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist"
            )

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote removed"}
