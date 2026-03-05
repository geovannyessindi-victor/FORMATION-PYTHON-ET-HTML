from datetime import datetime
from typing import List, Optional


class VIDEO:
    """Classe représentant une vidéo"""
    def __init__(self, videoid: str, title: str, url: str, duration: int, category: str):
        self.videoid = videoid
        self.title = title
        self.url = url
        self.duration = duration
        self.category = category
        self.likes = 0
        self.dislikes = 0
        self.comments: List['COMMENT'] = []
    
    def obtenir_id_video(self) -> str:
        return self.videoid
    
    def obtenir_titre(self) -> str:
        return self.title
    
    def obtenir_url(self) -> str:
        return self.url
    
    def obtenir_duree(self) -> int:
        return self.duration
    
    def obtenir_likes(self) -> int:
        return self.likes
    
    def obtenir_dislikes(self) -> int:
        return self.dislikes
    
    def obtenir_categorie(self) -> str:
        return self.category
    
    def obtenir_commentaires(self) -> List['COMMENT']:
        return self.comments
    
    def ajouter_like(self):
        self.likes += 1
    
    def retirer_like(self):
        if self.likes > 0:
            self.likes -= 1
    
    def ajouter_dislike(self):
        self.dislikes += 1
    
    def retirer_dislike(self):
        if self.dislikes > 0:
            self.dislikes -= 1
    
    def ajouter_commentaire(self, comment: 'COMMENT'):
        self.comments.append(comment)
    
    def retirer_commentaire(self, comment: 'COMMENT'):
        if comment in self.comments:
            self.comments.remove(comment)
    
    def lister_commentaires(self):
        print(f"\n=== Commentaires de la video: {self.title} ===")
        if not self.comments:
            print("Aucun commentaire")
            return
        for i, comment in enumerate(self.comments, 1):
            print(f"{i}. {comment.obtenir_contenu()} ({comment.obtenir_likes()} likes)")


class UTILISATEUR:
    """Classe représentant un utilisateur"""
    def __init__(self, userid: str, username: str, email: str, phone: str, password: str):
        self.userid = userid
        self.username = username
        self.email = email
        self.phone = phone
        self._password = password
        self.commentaires: List['COMMENT'] = []
        self.videos_aimees: List[VIDEO] = []
        self.videos_uploadees: List[VIDEO] = []
    
    def obtenir_id_utilisateur(self) -> str:
        return self.userid
    
    def obtenir_nom_utilisateur(self) -> str:
        return self.username
    
    def obtenir_email(self) -> str:
        return self.email
    
    def obtenir_telephone(self) -> str:
        return self.phone
    
    def obtenir_videos_aimees(self) -> List[VIDEO]:
        return self.videos_aimees
    
    def obtenir_commentaires(self) -> List['COMMENT']:
        return self.commentaires
    
    def obtenir_videos_uploadees(self) -> List[VIDEO]:
        return self.videos_uploadees
    
    def definir_nom_utilisateur(self, nouveau_nom: str):
        self.username = nouveau_nom
    
    def definir_telephone(self, nouveau_telephone: str):
        self.phone = nouveau_telephone
    
    def definir_email(self, nouveau_email: str):
        self.email = nouveau_email
    
    def enregistrer_utilisateur(self) -> bool:
        print(f"Utilisateur {self.username} enregistre avec succes!")
        return True
    
    def se_connecter(self, email_saisi: str, mot_de_passe_saisi: str) -> bool:
        if email_saisi == self.email and mot_de_passe_saisi == self._password:
            print(f"Utilisateur {self.username} connecte!")
            return True
        print(f"Echec de connexion pour {email_saisi}")
        return False
    
    def ajouter_commentaire(self, video: VIDEO, contenu: str) -> 'COMMENT':
        id_commentaire = f"C{len(self.commentaires) + 1}"
        commentaire = COMMENT(id_commentaire, self, video, contenu)
        self.commentaires.append(commentaire)
        video.ajouter_commentaire(commentaire)
        print(f"{self.username} a commente: {contenu}")
        return commentaire
    
    def supprimer_commentaire(self, commentaire: 'COMMENT'):
        if commentaire in self.commentaires:
            self.commentaires.remove(commentaire)
            commentaire.supprimer_commentaire()
    
    def aimer_video(self, video: VIDEO):
        if video not in self.videos_aimees:
            self.videos_aimees.append(video)
            video.ajouter_like()
            print(f"{self.username} a like la video: {video.obtenir_titre()}")
    
    def uploader_video(self, video: VIDEO):
        self.videos_uploadees.append(video)
        print(f"{self.username} a uploade la video: {video.obtenir_titre()}")
    
    def lister_mes_videos(self):
        print(f"\n=== Videos uploadees par {self.username} ===")
        if not self.videos_uploadees:
            print("Aucune video uploadee")
            return
        for i, video in enumerate(self.videos_uploadees, 1):
            print(f"{i}. {video.obtenir_titre()} ({video.obtenir_likes()} likes, "
                  f"{video.obtenir_dislikes()} dislikes)")
    
    def lister_mes_commentaires(self):
        print(f"\n=== Commentaires de {self.username} ===")
        if not self.commentaires:
            print("Aucun commentaire")
            return
        for i, commentaire in enumerate(self.commentaires, 1):
            print(f"{i}. {commentaire.obtenir_contenu()}")
    
    def rechercher_video(self, toutes_videos: List[VIDEO], mot_cle: str) -> Optional[VIDEO]:
        print(f"\n=== Recherche de: '{mot_cle}' ===")
        resultats = []
        
        for video in toutes_videos:
            if mot_cle.lower() in video.obtenir_titre().lower():
                resultats.append(video)
        
        if not resultats:
            print(f"Aucune video trouvee avec le mot-cle: {mot_cle}")
            return None
        
        print(f"Video(s) trouvee(s): {len(resultats)}")
        for i, video in enumerate(resultats, 1):
            print(f"{i}. {video.obtenir_titre()} - {video.obtenir_likes()} likes")
        
        return resultats[0]


class COMMENT:
    """Classe représentant un commentaire"""
    def __init__(self, commentid: str, auteur: UTILISATEUR, video: VIDEO, contenu: str):
        self.commentid = commentid
        self.auteur = auteur
        self.video = video
        self.contenu = contenu
        self.date = datetime.now()
        self.likes = 0
        self.dislikes = 0
        self.reponses: List['COMMENT'] = []
    
    def obtenir_id_commentaire(self) -> str:
        return self.commentid
    
    def obtenir_contenu(self) -> str:
        return self.contenu
    
    def obtenir_video(self) -> VIDEO:
        return self.video
    
    def obtenir_likes(self) -> int:
        return self.likes
    
    def obtenir_dislikes(self) -> int:
        return self.dislikes
    
    def ajouter_reponse(self, reponse: 'COMMENT'):
        self.reponses.append(reponse)
        print(f"Reponse ajoutee au commentaire {self.commentid}")
    
    def retirer_reponse(self, reponse: 'COMMENT'):
        if reponse in self.reponses:
            self.reponses.remove(reponse)
    
    def ajouter_like(self):
        self.likes += 1
    
    def retirer_like(self):
        if self.likes > 0:
            self.likes -= 1
    
    def modifier(self, nouveau_contenu: str):
        self.contenu = nouveau_contenu
        print(f"Commentaire {self.commentid} modifie")
    
    def supprimer_commentaire(self):
        self.video.retirer_commentaire(self)
        print(f"Commentaire {self.commentid} supprime")


class UTILISATEUR_PREMIUM(UTILISATEUR):
    """Classe représentant un utilisateur premium"""
    def __init__(self, userid: str, username: str, email: str, phone: str, 
                 password: str, type_abonnement: str):
        super().__init__(userid, username, email, phone, password)
        self.type_abonnement = type_abonnement
        self.debut_abonnement = datetime.now()
        self.fin_abonnement = None
        self.paiements: List['PAIEMENT'] = []
    
    def obtenir_type_abonnement(self) -> str:
        return self.type_abonnement
    
    def obtenir_paiements(self) -> List['PAIEMENT']:
        return self.paiements
    
    def renouveler_abonnement(self):
        self.debut_abonnement = datetime.now()
        print(f"Subscription renouvelee pour {self.obtenir_nom_utilisateur()}")
    
    def annuler_abonnement(self):
        self.fin_abonnement = datetime.now()
        print(f"Subscription annulee pour {self.obtenir_nom_utilisateur()}")
    
    def telecharger_video(self, video: VIDEO):
        print(f"Telechargement de '{video.obtenir_titre()}' en cours...")
    
    def ajouter_paiement(self, paiement: 'PAIEMENT'):
        self.paiements.append(paiement)
    
    def lister_paiements(self):
        print(f"\n=== Historique des paiements de {self.obtenir_nom_utilisateur()} ===")
        if not self.paiements:
            print("Aucun paiement")
            return
        total = 0
        for i, paiement in enumerate(self.paiements, 1):
            print(f"{i}. {paiement.obtenir_id_paiement()} - {paiement.obtenir_montant()} FCFA - "
                  f"{paiement.obtenir_statut()}")
            total += paiement.obtenir_montant()
        print(f"Total depense: {total} FCFA")


class PAIEMENT:
    """Classe représentant un paiement"""
    def __init__(self, paiementid: str, utilisateur: UTILISATEUR_PREMIUM, montant: float, 
                 methode_paiement: str):
        self.paiementid = paiementid
        self.utilisateur = utilisateur
        self.montant = montant
        self.methode_paiement = methode_paiement
        self.date_paiement = datetime.now()
        self.statut = "En attente"
    
    def obtenir_id_paiement(self) -> str:
        return self.paiementid
    
    def obtenir_montant(self) -> float:
        return self.montant
    
    def obtenir_statut(self) -> str:
        return self.statut
    
    def traiter_paiement(self) -> bool:
        self.statut = "Complete"
        self.utilisateur.ajouter_paiement(self)
        print(f"Paiement de {self.montant} FCFA traite avec succes!")
        return True
    
    def rembourser(self):
        self.statut = "Rembourse"
        print(f"Paiement {self.paiementid} rembourse")
    
    def obtenir_recu(self) -> str:
        return f"Recu: {self.paiementid} - Montant: {self.montant} FCFA"


# ========== FONCTIONS GLOBALES ==========

def lister_toutes_videos(videos: List[VIDEO]):
    """Liste toutes les vidéos disponibles"""
    print("\n=== LISTE DE TOUTES LES VIDEOS ===")
    if not videos:
        print("Aucune video disponible")
        return
    for i, video in enumerate(videos, 1):
        print(f"{i}. {video.obtenir_titre()} - Categorie: {video.obtenir_categorie()} - "
              f"Duree: {video.obtenir_duree()} min - Likes: {video.obtenir_likes()} - "
              f"Commentaires: {len(video.obtenir_commentaires())}")
    print(f"\nTotal: {len(videos)} video(s)")


def rechercher_par_categorie(videos: List[VIDEO], categorie: str) -> List[VIDEO]:
    """Recherche des vidéos par catégorie"""
    print(f"\n=== Recherche par categorie: '{categorie}' ===")
    resultats = []
    
    for video in videos:
        if categorie.lower() in video.obtenir_categorie().lower():
            resultats.append(video)
    
    if not resultats:
        print("Aucune video trouvee dans cette categorie")
    else:
        print(f"{len(resultats)} video(s) trouvee(s):")
        for i, video in enumerate(resultats, 1):
            print(f"{i}. {video.obtenir_titre()}")
    
    return resultats


# =========== PROGRAMME PRINCIPAL =========

def main():
    print("===============================================")
    print("|| GET VIDEO YOUTUBE USEFULNESS AUTOMATICALLY ||")
    print("===============================================")
    
    print("\n--- CREATION DES UTILISATEURS ---")
    utilisateur1 = UTILISATEUR("A001", "VICTOR", "geovanny@gmail.com", "+237692705083", "Geovanny2005#")
    utilisateur1.enregistrer_utilisateur()
    
    utilisateur2 = UTILISATEUR("S003", "MERLINE", "merline@gmail.com", "+237688256263", "DAT2024")
    utilisateur2.enregistrer_utilisateur()
    
    print("\n--- CREATION DES VIDEOS ---")
    video1 = VIDEO("V001", "POO: Heritage et Polymorphisme", "https://video.url/1", 60, "Educatif")
    video2 = VIDEO("V002", "Introduction a C++", "https://video.url/2", 45, "Educatif")
    video3 = VIDEO("V003", "Tutoriel Python Avance", "https://video.url/3", 90, "Programmation")
    
    print("3 videos creees avec succes!")
    
    utilisateur1.uploader_video(video1)
    utilisateur1.uploader_video(video2)
    utilisateur2.uploader_video(video3)
    
    toutes_videos = [video1, video2, video3]
    lister_toutes_videos(toutes_videos)
    
    print("\n--- INTERACTIONS VIDEOS ---")
    utilisateur2.aimer_video(video1)
    utilisateur2.aimer_video(video2)
    utilisateur1.aimer_video(video3)
    
    print("\n--- COMMENTAIRES ---")
    commentaire1 = utilisateur2.ajouter_commentaire(video1, "Excellente video, tres instructive!")
    commentaire1.ajouter_like()
    commentaire1.ajouter_like()
    
    commentaire2 = utilisateur1.ajouter_commentaire(video3, "Merci pour ce tutoriel complet!")
    commentaire2.ajouter_like()
    
    commentaire3 = utilisateur2.ajouter_commentaire(video2, "Parfait pour les debutants!")
    
    video1.lister_commentaires()
    video2.lister_commentaires()
    
    utilisateur1.lister_mes_videos()
    utilisateur2.lister_mes_videos()
    utilisateur2.lister_mes_commentaires()
    
    video_trouvee = utilisateur1.rechercher_video(toutes_videos, "POO")
    if video_trouvee:
        print(f"\nVideo selectionnee: {video_trouvee.obtenir_titre()}")
    
    videos_educatives = rechercher_par_categorie(toutes_videos, "Educatif")
    
    print("\n--- UPGRADE PREMIUM ---")
    utilisateur_premium = UTILISATEUR_PREMIUM(utilisateur2.obtenir_id_utilisateur(), 
                                              utilisateur2.obtenir_nom_utilisateur(),
                                              utilisateur2.obtenir_email(), 
                                              utilisateur2.obtenir_telephone(),
                                              "DAT2024", "Mensuel")
    print(f"{utilisateur_premium.obtenir_nom_utilisateur()} est maintenant utilisateur premium!")
    
    print("\n--- PAIEMENTS ---")
    paiement1 = PAIEMENT("P001", utilisateur_premium, 9990, "Carte bancaire")
    paiement1.traiter_paiement()
    
    paiement2 = PAIEMENT("P002", utilisateur_premium, 9990, "Mobile Money")
    paiement2.traiter_paiement()
    
    utilisateur_premium.lister_paiements()
    
    print("\n--- FONCTIONNALITES PREMIUM ---")
    utilisateur_premium.telecharger_video(video1)
    utilisateur_premium.telecharger_video(video3)
    
    print("\n========================================")
    print("         STATISTIQUES FINALES           ")
    print("========================================")
    print(f"Total videos: {len(toutes_videos)}")
    print("Total utilisateurs: 2 (dont 1 premium)")
    print("\nDetails des videos:")
    for video in toutes_videos:
        print(f"\n- {video.obtenir_titre()}")
        print(f"  Likes: {video.obtenir_likes()}")
        print(f"  Dislikes: {video.obtenir_dislikes()}")
        print(f"  Commentaires: {len(video.obtenir_commentaires())}")
    
    print("\n===============================================")
    print("    Programme termine avec succes!            ")
    print("===============================================")


if __name__ == "__main__":
    main()